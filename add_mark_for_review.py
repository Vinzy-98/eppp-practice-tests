#!/usr/bin/env python3
"""
Add 'Mark for Review' functionality to all test files
"""
import os
import glob
import re

def add_mark_for_review(filepath):
    """Add mark for review functionality to a test file"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has mark for review
        if 'function toggleReview(' in content:
            print(f"✓ Already has mark for review: {os.path.basename(filepath)}")
            return False
        
        # Step 1: Add CSS for review button and marked state
        css_addition = """
        .question.marked-review {
            border-left-color: #f39c12;
            background: #fff8e6;
        }
        
        .review-btn {
            background: #f39c12;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9em;
            margin-top: 10px;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        
        .review-btn:hover {
            background: #e67e22;
            transform: translateY(-1px);
        }
        
        .review-btn.marked {
            background: #27ae60;
        }
        
        .review-btn.marked:hover {
            background: #229954;
        }
        
        .review-summary {
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
            display: none;
        }
        
        .review-summary.show {
            display: block;
        }
        
        .review-summary h3 {
            color: #856404;
            margin-bottom: 10px;
        }
        
        .review-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        
        .review-link {
            background: #f39c12;
            color: white;
            padding: 6px 12px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.2s;
        }
        
        .review-link:hover {
            background: #e67e22;
            transform: translateY(-2px);
        }
"""
        
        # Insert CSS before closing </style> tag
        content = re.sub(
            r'(</style>)',
            css_addition + r'        \1',
            content,
            count=1
        )
        
        # Step 2: Add review button HTML after result-indicator in each question
        # This is tricky because we need to add it to all questions
        # We'll do this with a regex that finds the pattern
        content = re.sub(
            r'(<div class="result-indicator"></div>)\s*</div>\s*\n\s*<div class="question"',
            r'\1\n                <button class="review-btn" onclick="toggleReview(this)">🔖 Mark for Review</button>\n            </div>\n\n            <div class="question"',
            content
        )
        
        # Also add to the last question (different pattern)
        content = re.sub(
            r'(<div class="result-indicator"></div>)\s*</div>\s*\n\s*</div>\s*</div>\s*<script',
            r'\1\n                <button class="review-btn" onclick="toggleReview(this)">🔖 Mark for Review</button>\n            </div>\n\n        </div>\n    </div>\n    \n    <script',
            content
        )
        
        # Step 3: Add review summary div after progress bar
        review_summary_html = """
        
        <div class="review-summary" id="reviewSummary">
            <h3>📋 Questions Marked for Review</h3>
            <div class="review-links" id="reviewLinks"></div>
        </div>
"""
        
        # Insert after progress bar
        content = re.sub(
            r'(<div class="progress-fill" id="progressBar">0%</div>\s*</div>)',
            r'\1' + review_summary_html,
            content,
            count=1
        )
        
        # Step 4: Add JavaScript functions
        js_functions = """
        // Mark for Review functionality
        function toggleReview(button) {
            const question = button.closest('.question');
            const questionNum = question.dataset.question;
            
            if (question.classList.contains('marked-review')) {
                // Unmark
                question.classList.remove('marked-review');
                button.textContent = '🔖 Mark for Review';
                button.classList.remove('marked');
            } else {
                // Mark
                question.classList.add('marked-review');
                button.textContent = '✓ Marked for Review';
                button.classList.add('marked');
            }
            
            updateReviewSummary();
        }
        
        function updateReviewSummary() {
            const markedQuestions = document.querySelectorAll('.question.marked-review');
            const summary = document.getElementById('reviewSummary');
            const linksContainer = document.getElementById('reviewLinks');
            
            if (markedQuestions.length > 0) {
                summary.classList.add('show');
                linksContainer.innerHTML = '';
                
                markedQuestions.forEach(q => {
                    const questionNum = q.dataset.question;
                    const link = document.createElement('a');
                    link.href = '#';
                    link.className = 'review-link';
                    link.textContent = `Q${questionNum}`;
                    link.onclick = function(e) {
                        e.preventDefault();
                        q.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    };
                    linksContainer.appendChild(link);
                });
            } else {
                summary.classList.remove('show');
            }
        }
        
"""
        
        # Insert before the existing selectChoice function
        content = re.sub(
            r'(\n\s+function selectChoice\(choiceElement\))',
            js_functions + r'\1',
            content,
            count=1
        )
        
        # Save the modified content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added mark for review: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    # Get all test files
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Adding 'Mark for Review' functionality...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_mark_for_review(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
