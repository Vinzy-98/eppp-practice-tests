#!/usr/bin/env python3
"""
Parse EPPP test files (DOCX and PDF) into JSON format for the web app.
"""
import os
import re
import json
import docx
import pdfplumber

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "eppp_app", "data")

def slugify(name):
    """Create a URL-safe slug from a test name."""
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    s = re.sub(r'[\s]+', '-', s.strip())
    return s.lower()

# ─── DOCX PARSER (AATBS format with "Question ID" lines) ───────────────────

def parse_docx_aatbs(filepath):
    """Parse DOCX files that use the AATBS 'Question ID #...' format."""
    doc = docx.Document(filepath)
    paragraphs = [p.text for p in doc.paragraphs]

    questions = []
    i = 0
    while i < len(paragraphs):
        text = paragraphs[i].strip()

        # Look for "Question ID #..." line
        if text.startswith("Question ID"):
            # Extract question text (everything after "Question ID #NNNN: ")
            q_match = re.match(r'Question ID #\d+:\s*(.*)', text)
            if q_match:
                question_text = q_match.group(1).strip()
            else:
                question_text = text
            
            i += 1
            # Skip "Question NSelect one:" or "Select one:" line
            while i < len(paragraphs):
                line = paragraphs[i].strip()
                if line.startswith('Select one') or 'Select one' in line:
                    i += 1
                    break
                # Sometimes question text continues on the next line before Select one
                if not line.startswith('A.') and line and 'Select one' not in line:
                    question_text += " " + line
                    i += 1
                else:
                    break

            # Parse options A, B, C, D (and sometimes E)
            options = {}
            current_letter = None
            while i < len(paragraphs):
                line = paragraphs[i].strip()
                # Check for option letter line like "A." or "B."
                letter_match = re.match(r'^([A-E])\.\s*$', line)
                if letter_match:
                    current_letter = letter_match.group(1)
                    i += 1
                    # Next line is the option text
                    if i < len(paragraphs):
                        options[current_letter] = paragraphs[i].strip()
                        i += 1
                    continue
                # Check for inline option like "A. some text"
                inline_match = re.match(r'^([A-E])\.\s+(.+)', line)
                if inline_match:
                    current_letter = inline_match.group(1)
                    options[current_letter] = inline_match.group(2).strip()
                    i += 1
                    continue
                # Check for Feedback marker or Correct Answer
                if line == 'Feedback' or line.startswith('Correct Answer') or line.startswith('The correct answer'):
                    break
                # If we already have options and hit something else, break
                if options and not letter_match:
                    break
                i += 1

            # Parse correct answer and explanation
            correct_answer = None
            explanation_lines = []
            while i < len(paragraphs):
                line = paragraphs[i].strip()
                if line == 'Feedback':
                    i += 1
                    continue

                # "Correct Answer is: X" format
                ca_match = re.match(r'Correct Answer is:\s*([A-E])', line)
                if ca_match:
                    correct_answer = ca_match.group(1)
                    # Rest of this line is start of explanation
                    rest = line[ca_match.end():].strip().lstrip('\n')
                    if rest:
                        explanation_lines.append(rest)
                    i += 1
                    continue

                # "The correct answer is X." format
                ca_match2 = re.match(r'The correct answer is ([A-E])\.?', line)
                if ca_match2:
                    correct_answer = ca_match2.group(1)
                    rest = line[ca_match2.end():].strip().lstrip('.')
                    if rest:
                        explanation_lines.append(rest)
                    i += 1
                    continue

                # Next question marker - stop
                if re.match(r'^Question \d+$', line):
                    break
                if line.startswith('Question ID'):
                    break

                # Skip metadata lines
                if line in ('Not answered', 'Flag question', 'Question text', '') or \
                   line.startswith('Marked out of') or line.startswith('Mark ') or \
                   line == 'Correct' or line == 'Incorrect':
                    i += 1
                    continue

                # Explanation text
                if correct_answer is not None and line:
                    explanation_lines.append(line)
                    i += 1
                    continue

                i += 1

            if question_text and options and correct_answer:
                questions.append({
                    "question": question_text,
                    "options": options,
                    "correct": correct_answer,
                    "explanation": "\n".join(explanation_lines).strip()
                })
        else:
            i += 1

    return questions


# ─── PDF PARSER (AATBS format) ─────────────────────────────────────────────

def parse_pdf_aatbs(filepath):
    """Parse PDF files from AATBS with Question ID format."""
    pdf = pdfplumber.open(filepath)
    
    # Extract all text
    full_text = ""
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            # Remove header/footer lines
            lines = text.split('\n')
            filtered = []
            for line in lines:
                # Skip page headers/footers
                if 'Attempt review | AATBS' in line:
                    continue
                if line.strip().startswith('https://moodle.cloud'):
                    continue
                if re.match(r'^\d+/\d+/\d+,\s+\d+:\d+\s+(AM|PM)', line.strip()):
                    continue
                if re.match(r'^\d+/\d+$', line.strip()):
                    continue
                filtered.append(line)
            full_text += "\n".join(filtered) + "\n"
    
    pdf.close()
    
    # Split by "Question ID" markers
    # Pattern: Question ID #NNNNN:
    parts = re.split(r'(Question ID #\d+:)', full_text)
    
    questions = []
    for idx in range(1, len(parts), 2):
        if idx + 1 >= len(parts):
            break
        
        q_id_prefix = parts[idx]  # "Question ID #NNNNN:"
        q_body = parts[idx + 1]
        
        lines = q_body.strip().split('\n')
        
        # First lines until "Select one:" are the question text
        question_text = ""
        line_idx = 0
        while line_idx < len(lines):
            line = lines[line_idx].strip()
            if line.startswith("Select one") or line == "Select one:":
                line_idx += 1
                break
            question_text += " " + line
            line_idx += 1
        question_text = question_text.strip()
        
        # Parse options - format is 'A. text or lines with A.\ntext
        options = {}
        current_letter = None
        current_text = ""
        
        while line_idx < len(lines):
            line = lines[line_idx].strip()
            
            # Check for option line like "'A. text" or ";A. text" or "✓"
            opt_match = re.match(r"^[';✓\s]*([A-E])\.\s*(.*)", line)
            
            if opt_match:
                if current_letter:
                    options[current_letter] = current_text.strip()
                current_letter = opt_match.group(1)
                current_text = opt_match.group(2)
                # Remove checkmarks and other markers
                current_text = re.sub(r'[✓✗×]', '', current_text).strip()
                if current_text.endswith('Correct') or current_text.endswith('Incorrect'):
                    current_text = re.sub(r'\s*(Correct|Incorrect)$', '', current_text).strip()
                line_idx += 1
                continue
            
            # Check for "The correct answer is" 
            if line.startswith('The correct answer is') or line.startswith('Correct Answer is'):
                if current_letter:
                    options[current_letter] = current_text.strip()
                break
            
            # Continuation of current option text
            if current_letter and line:
                cleaned = re.sub(r'[✓✗×]', '', line).strip()
                if cleaned.endswith('Correct') or cleaned.endswith('Incorrect'):
                    cleaned = re.sub(r'\s*(Correct|Incorrect)$', '', cleaned).strip()
                current_text += " " + cleaned
            
            line_idx += 1
        
        # Parse correct answer
        correct_answer = None
        explanation_lines = []
        
        while line_idx < len(lines):
            line = lines[line_idx].strip()
            
            ca_match = re.match(r'(?:The correct answer is|Correct Answer is:?)\s*([A-E])\.?', line)
            if ca_match:
                correct_answer = ca_match.group(1)
                line_idx += 1
                continue
            
            # Stop at next question
            if re.match(r'^Question \d+$', line):
                break
            if line.startswith('Question ID'):
                break
            
            # Skip metadata
            if line in ('', 'Not answered', 'Correct', 'Incorrect', 'Flag question', 'Question text', 'Feedback') or \
               line.startswith('Marked out of') or line.startswith('Mark '):
                line_idx += 1
                continue
            
            if correct_answer is not None and line:
                explanation_lines.append(line)
            
            line_idx += 1
        
        if question_text and options and correct_answer:
            questions.append({
                "question": question_text,
                "options": options,
                "correct": correct_answer,
                "explanation": "\n".join(explanation_lines).strip()
            })
    
    return questions


def get_test_name(filename):
    """Extract a clean test name from a filename."""
    name = os.path.splitext(filename)[0]
    # Remove common suffixes
    name = re.sub(r'_?\s*Attempt review.*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*_\s*AATBS\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Answers?\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*with answers?\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(page \d+ of \d+\)', '', name, flags=re.IGNORECASE)
    # Clean up underscores used as separators
    name = re.sub(r'_\s*', ' / ', name)
    # But fix leading separator from filenames starting with year
    name = re.sub(r'^(\d{4})\s*/\s*', r'\1 ', name)
    # Clean up multiple spaces
    name = re.sub(r'\s+', ' ', name)
    return name.strip()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    all_tests = []
    
    # Process Category Tests
    cat_dir = os.path.join(BASE_DIR, "Category_Tests")
    full_dir = os.path.join(BASE_DIR, "Full_Tests")
    
    for category, directory in [("Category Tests", cat_dir), ("Full Tests", full_dir)]:
        if not os.path.isdir(directory):
            continue
        
        for filename in sorted(os.listdir(directory)):
            filepath = os.path.join(directory, filename)
            if filename.startswith('.'):
                continue
            
            test_name = get_test_name(filename)
            slug = slugify(test_name)
            
            print(f"Processing: {filename}")
            
            questions = []
            try:
                if filename.endswith('.docx'):
                    questions = parse_docx_aatbs(filepath)
                elif filename.endswith('.pdf'):
                    questions = parse_pdf_aatbs(filepath)
                else:
                    print(f"  Skipping unsupported format: {filename}")
                    continue
            except Exception as e:
                print(f"  ERROR parsing {filename}: {e}")
                continue
            
            if not questions:
                print(f"  WARNING: No questions parsed from {filename}")
                continue
            
            print(f"  Parsed {len(questions)} questions")
            
            # Write individual test JSON
            test_file = os.path.join(OUTPUT_DIR, f"{slug}.json")
            with open(test_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "name": test_name,
                    "slug": slug,
                    "category": category,
                    "questionCount": len(questions),
                    "questions": questions
                }, f, indent=2, ensure_ascii=False)
            
            all_tests.append({
                "name": test_name,
                "slug": slug,
                "category": category,
                "questionCount": len(questions),
                "file": f"data/{slug}.json"
            })
    
    # Write manifest
    manifest_path = os.path.join(OUTPUT_DIR, "..", "tests-manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(all_tests, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*50}")
    print(f"Total tests: {len(all_tests)}")
    total_q = sum(t['questionCount'] for t in all_tests)
    print(f"Total questions: {total_q}")
    print(f"Manifest: {manifest_path}")
    print(f"Data dir: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
