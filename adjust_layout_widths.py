#!/usr/bin/env python3
"""
Adjust layout widths:
- Top container: centered with max-width 1200px
- Questions container: expand to fill available space (no max-width)
"""

import os
import re

# Test files to update (skip AR_Exam_1 since we already did it manually)
test_files = [
    'AR_Exam_2.html', 'AR_Exam_3.html', 'AR_Exam_4.html',
    'AR_Exam_5.html', 'AR_Exam_6.html', 'AR_Exam_7.html', 'AR_Exam_8.html',
    'Practice_EPPP_1.html', 'Practice_EPPP_2.html', 'Practice_EPPP_3.html',
    'Practice_EPPP_4.html', 'Practice_EPPP_5.html', 'Practice_EPPP_6.html',
    'Practice_EPPP_7.html'
]

def adjust_widths(filename):
    """Adjust container widths."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update .top-container - center with max-width
    top_container_pattern = r'\.top-container\s*{[^}]*}'
    top_container_css = '''.top-container {
            max-width: 1200px;
            margin: 0 auto 20px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }'''
    
    if re.search(top_container_pattern, content):
        content = re.sub(top_container_pattern, top_container_css, content)
        print(f"  ✓ Updated .top-container")
    
    # 2. Update .container - expand to fill space, no max-width
    container_pattern = r'\.container\s*{[^}]*?}'
    container_css = '''.container {
            flex: 1;
            margin: 0 20px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow-y: auto;
        }'''
    
    if re.search(container_pattern, content):
        content = re.sub(container_pattern, container_css, content, count=1)
        print(f"  ✓ Updated .container")
    
    # 3. Update body.has-sidebar .container rule
    sidebar_pattern = r'body\.has-sidebar\s+\.container\s*{[^}]*?}'
    sidebar_css = '''body.has-sidebar .container {
            margin-left: 0;
        }'''
    
    if re.search(sidebar_pattern, content):
        content = re.sub(sidebar_pattern, sidebar_css, content)
        print(f"  ✓ Updated body.has-sidebar .container")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Update all test files."""
    print("Adjusting layout widths...\n")
    
    updated_count = 0
    for filename in test_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if adjust_widths(filename):
                updated_count += 1
            print()
    
    print(f"\n✅ Updated {updated_count} files successfully")

if __name__ == '__main__':
    main()
