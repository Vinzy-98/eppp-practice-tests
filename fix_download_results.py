#!/usr/bin/env python3
"""
Fix downloadResults() function - change textContent to innerHTML for scoreDetails
"""
import os
import glob
import re

def fix_download_function(filepath):
    """Fix the downloadResults function in a test file"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the bug exists
        if "scoreDetails').textContent.replace" not in content:
            print(f"✓ Already fixed or different format: {os.path.basename(filepath)}")
            return False
        
        # Fix: Change textContent to innerHTML in downloadResults
        old_code = "const scoreDetails = document.getElementById('scoreDetails').textContent.replace(/<br>/g, '\\n');"
        new_code = "const scoreDetails = document.getElementById('scoreDetails').innerHTML.replace(/<br>/g, '\\n');"
        
        if old_code in content:
            content = content.replace(old_code, new_code)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed download function: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠ Pattern not found in expected format: {os.path.basename(filepath)}")
            return False
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    # Get all test files
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Fixing download results function...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_download_function(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Fixed {total_updated} files.\n")

if __name__ == '__main__':
    main()
