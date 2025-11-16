#!/usr/bin/env python3
"""
Move the button-container (Results and Other options) back to the top of the page,
outside the flexbox layout, so it appears above both the sidebar and main content.
"""

import os
import re

# Test files to update
test_files = [
    'AR_Exam_1.html', 'AR_Exam_2.html', 'AR_Exam_3.html', 'AR_Exam_4.html',
    'AR_Exam_5.html', 'AR_Exam_6.html', 'AR_Exam_7.html', 'AR_Exam_8.html',
    'Practice_EPPP_1.html', 'Practice_EPPP_2.html', 'Practice_EPPP_3.html',
    'Practice_EPPP_4.html', 'Practice_EPPP_5.html', 'Practice_EPPP_6.html',
    'Practice_EPPP_7.html'
]

def move_buttons_to_top(filename):
    """Move button-container outside the main flexbox container."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update body CSS to wrap flexbox content
    body_css_pattern = r'(body\s*{[^}]*?)(display:\s*flex;)'
    body_css_replacement = r'\1/* Flexbox for sidebar + content only */\n            \2'
    content = re.sub(body_css_pattern, body_css_replacement, content)
    
    # Add CSS for main-wrapper to contain the flexbox layout
    container_css = r'(body\.has-sidebar\s+\.container\s*{[^}]*?})'
    main_wrapper_css = r'''\1
        
        .top-section {
            background: white;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin: 0 20px 20px 20px;
        }
        
        .main-wrapper {
            display: flex;
            flex: 1;
            min-height: 0;
        }'''
    
    content = re.sub(container_css, main_wrapper_css, content)
    
    # Update container CSS to remove flex-grow and work inside main-wrapper
    container_pattern = r'(\.container\s*{[^}]*?)flex:\s*1;([^}]*?})'
    container_replacement = r'\1/* Container inside main-wrapper */\2'
    content = re.sub(container_pattern, container_replacement, content)
    
    # Find and extract the button-container HTML (including progress bar)
    button_container_pattern = r'(<div class="button-container">.*?</div>\s*</div>)'
    button_match = re.search(button_container_pattern, content, re.DOTALL)
    
    if button_match:
        button_html = button_match.group(1)
        
        # Remove button-container from its current location
        content = re.sub(button_container_pattern, '', content, count=1, flags=re.DOTALL)
        
        # Find where to insert it - after exam-info, before container close
        # Actually, we need to restructure the HTML completely
        
        # Find the structure: <body> ... <div class="container"> <h1> <exam-info>
        body_start_pattern = r'(<body>\s*<div class="container">.*?<div class="exam-info">.*?</div>)'
        body_match = re.search(body_start_pattern, content, re.DOTALL)
        
        if body_match:
            header_section = body_match.group(1)
            
            # Create the new structure
            new_structure = f'''<body>
    <div class="top-section">
{header_section.replace('<body>', '').replace('<div class="container">', '').strip()}
        
        {button_html}
    </div>
    
    <div class="main-wrapper">
        <div class="review-summary" id="reviewSummary">
            <h3>📋 Questions Marked for Review</h3>
            <div class="review-links" id="reviewLinks"></div>
        </div>
        
        <div class="container">'''
            
            # Replace the old structure
            content = re.sub(body_start_pattern + r'.*?(<div class="button-container">.*?</div>\s*</div>)\s*<div class="review-summary"', 
                           new_structure.replace('\\', '\\\\') + r'        <div class="results-summary"',
                           content, count=1, flags=re.DOTALL)
            
            print(f"  ✓ Moved button-container to top section")
        else:
            print(f"  ⚠ Could not find header section")
    else:
        print(f"  ⚠ Could not find button-container")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Update all test files."""
    print("Moving button-container to top of page...\n")
    
    updated_count = 0
    for filename in test_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if move_buttons_to_top(filename):
                updated_count += 1
            print()
    
    print(f"\n✅ Updated {updated_count} files successfully")

if __name__ == '__main__':
    main()
