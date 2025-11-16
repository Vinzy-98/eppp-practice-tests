#!/usr/bin/env python3
"""
Fix the two-column layout properly by ensuring body uses display: flex
and container doesn't overlap with the sidebar.
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

def fix_layout(filename):
    """Fix the two-column layout in a test file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace body CSS to add display: flex
    body_css_pattern = r'(body\s*{[^}]*?)(padding:\s*20px;)'
    body_css_replacement = r'\1display: flex;\n            min-height: 100vh;\n            \2'
    
    if re.search(body_css_pattern, content):
        content = re.sub(body_css_pattern, body_css_replacement, content)
        print(f"  ✓ Added display: flex to body")
    else:
        print(f"  ⚠ Body CSS pattern not found")
    
    # Update container CSS to ensure proper spacing
    container_css_pattern = r'(\.container\s*{[^}]*?)(flex:\s*1;)'
    container_css_replacement = r'\1\2\n            margin-left: 0;\n            transition: margin-left 0.3s ease;'
    
    if re.search(container_css_pattern, content):
        content = re.sub(container_css_pattern, container_css_replacement, content)
        print(f"  ✓ Updated container CSS")
    
    # Make sure body.has-sidebar rule is correct
    sidebar_margin_pattern = r'body\.has-sidebar\s+\.container\s*{[^}]*?margin-left:\s*170px;[^}]*?}'
    if not re.search(sidebar_margin_pattern, content):
        print(f"  ⚠ Sidebar margin rule needs verification")
    
    # Update review-summary to NOT be overlapping
    # Change from fixed overlay to proper column
    review_summary_pattern = r'(\.review-summary\s*{[^}]*?)position:\s*fixed;([^}]*?)left:\s*0;([^}]*?)top:\s*0;([^}]*?)width:\s*150px;([^}]*?)height:\s*100vh;'
    review_summary_replacement = r'\1position: fixed;\2left: 0;\3top: 0;\4width: 150px;\5height: 100vh;\n            flex-shrink: 0;'
    
    content = re.sub(review_summary_pattern, review_summary_replacement, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Update all test files."""
    print("Fixing two-column layout in all test files...\n")
    
    updated_count = 0
    for filename in test_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if fix_layout(filename):
                updated_count += 1
            print()
    
    print(f"\n✅ Updated {updated_count} files successfully")

if __name__ == '__main__':
    main()
