#!/usr/bin/env python3
"""
Restructure HTML to move header/buttons to top, with sidebar+content in flexbox below.
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

def restructure_layout(filename):
    """Restructure the HTML layout."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update body CSS - remove flexbox
    content = re.sub(
        r'(body\s*{[^}]*?)display:\s*flex;\s*min-height:\s*100vh;\s*',
        r'\1',
        content
    )
    
    # 2. Add new CSS classes before </style>
    css_addition = '''
        .top-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin: 0 20px 20px 20px;
        }
        
        .main-layout {
            display: flex;
            flex: 1;
            min-height: 0;
        }
        '''
    
    content = re.sub(r'(\s+)</style>', r'\1' + css_addition + r'\1</style>', content)
    
    # 3. Find and restructure HTML
    # Pattern: <body> ... <div class="container"> ... button-container ... </div> ... <div class="review-summary">
    
    # Extract the header section (user-panel through button-container)
    header_pattern = r'<body>\s*<div class="container">\s*(.*?)<div class="button-container">(.*?)</div>\s*</div>\s*<div class="review-summary"'
    header_match = re.search(header_pattern, content, re.DOTALL)
    
    if header_match:
        header_content = header_match.group(1)
        button_content = header_match.group(2)
        
        # Create new structure
        new_structure = f'''<body>
    
    <div class="top-container">
        {header_content.strip()}
        
        <div class="button-container">
            {button_content.strip()}
        </div>
    </div>

    <div class="main-layout">
        <div class="review-summary"'''
        
        # Replace old structure
        content = re.sub(header_pattern, new_structure, content, flags=re.DOTALL)
        
        # Add wrapper div for container
        content = re.sub(
            r'(<div class="review-summary".*?</div>\s*)<div class="results-summary"',
            r'\1\n\n        <div class="container">\n        <div class="results-summary"',
            content,
            count=1,
            flags=re.DOTALL
        )
        
        # Close the divs at the end
        content = re.sub(
            r'(</script>)\s*</body>',
            r'\1\n    </div> <!-- Close container -->\n    </div> <!-- Close main-layout -->\n</body>',
            content
        )
        
        print(f"  ✓ Restructured layout successfully")
    else:
        print(f"  ⚠ Could not find structure pattern")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Update all test files."""
    print("Restructuring layout: moving buttons to top...\n")
    
    updated_count = 0
    for filename in test_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if restructure_layout(filename):
                updated_count += 1
            print()
    
    print(f"\n✅ Updated {updated_count} files successfully")

if __name__ == '__main__':
    main()
