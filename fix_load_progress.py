#!/usr/bin/env python3
"""
Fix loadProgress() call in all test files
"""
import os
import glob

def fix_load_progress_call(filepath):
    """Add loadProgress() call to window load event"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has loadProgress() call
        if "loadProgress(); // Check for saved progress" in content:
            print(f"✓ Already fixed: {os.path.basename(filepath)}")
            return False
        
        # Check if has loadProgress function
        if "function loadProgress()" not in content:
            print(f"✗ No loadProgress function: {os.path.basename(filepath)}")
            return False
        
        # Find and replace the window load event
        old_pattern = """        window.addEventListener('load', function() {
            initializeUser();
        });"""
        
        new_pattern = """        window.addEventListener('load', function() {
            initializeUser();
            loadProgress(); // Check for saved progress
        });"""
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed: {os.path.basename(filepath)}")
            return True
        else:
            print(f"✗ Could not find pattern: {os.path.basename(filepath)}")
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
    
    total_fixed = 0
    
    print("\n🔄 Fixing loadProgress() calls...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_load_progress_call(filepath):
                total_fixed += 1
    
    print(f"\n✅ Complete! Fixed {total_fixed} files.\n")

if __name__ == '__main__':
    main()
