#!/usr/bin/env python3
"""
Fix saveTestResults to use h1 instead of .exam-title
Also fix similar issues in other functions
"""
import os
import glob
import re

def fix_exam_title_selector(filepath):
    """Fix the exam title selector in test files"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Fix in saveTestResults function
        if "querySelector('.exam-title')" in content:
            content = content.replace(
                "const examTitle = document.querySelector('.exam-title').textContent;",
                "const examTitle = document.querySelector('h1').textContent;"
            )
            changes_made.append('saveTestResults')
        
        # Fix in loadAttemptNumber function if exists
        content = re.sub(
            r"const examTitle = document\.querySelector\('\.exam-title'\)\.textContent;",
            "const examTitle = document.querySelector('h1').textContent;",
            content
        )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed exam title selector: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠ No changes needed: {os.path.basename(filepath)}")
            return False
        
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
    
    print("\n🔄 Fixing exam title selectors...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_exam_title_selector(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Fixed {total_updated} files.\n")

if __name__ == '__main__':
    main()
