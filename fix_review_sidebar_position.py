#!/usr/bin/env python3
"""
Fix review sidebar to be part of flex layout instead of fixed positioning.
This prevents it from overlapping the questions.
"""

import os
import re

# Test files to update (skip AR_Exam_1 since we already fixed it)
test_files = [
    'AR_Exam_2.html', 'AR_Exam_3.html', 'AR_Exam_4.html',
    'AR_Exam_5.html', 'AR_Exam_6.html', 'AR_Exam_7.html', 'AR_Exam_8.html',
    'Practice_EPPP_1.html', 'Practice_EPPP_2.html', 'Practice_EPPP_3.html',
    'Practice_EPPP_4.html', 'Practice_EPPP_5.html', 'Practice_EPPP_6.html',
    'Practice_EPPP_7.html'
]

def fix_review_sidebar(filename):
    """Fix review sidebar positioning."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the .review-summary CSS
    review_summary_pattern = r'\.review-summary\s*{[^}]*?}'
    review_summary_css = '''.review-summary {
            width: 170px;
            flex-shrink: 0;
            background: #fff3cd;
            border-right: 3px solid #f39c12;
            padding: 20px 15px;
            display: none;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            overflow-y: auto;
            max-height: calc(100vh - 40px);
            position: sticky;
            top: 20px;
        }'''
    
    if re.search(review_summary_pattern, content):
        content = re.sub(review_summary_pattern, review_summary_css, content, count=1)
        print(f"  ✓ Updated .review-summary CSS")
    
    # Update .review-summary.show
    show_pattern = r'\.review-summary\.show\s*{[^}]*?}'
    show_css = '''.review-summary.show {
            display: flex;
            flex-direction: column;
        }'''
    
    if re.search(show_pattern, content):
        content = re.sub(show_pattern, show_css, content)
        print(f"  ✓ Updated .review-summary.show CSS")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Update all test files."""
    print("Fixing review sidebar positioning...\n")
    
    updated_count = 0
    for filename in test_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if fix_review_sidebar(filename):
                updated_count += 1
            print()
    
    print(f"\n✅ Updated {updated_count} files successfully")

if __name__ == '__main__':
    main()
