#!/usr/bin/env python3
"""
Fix dashboard link in all test files
"""
import os
import glob

def fix_dashboard_link(filepath):
    """Fix the dashboard link path"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already fixed
        if "window.location.href = 'dashboard.html';" in content:
            print(f"✓ Already fixed: {os.path.basename(filepath)}")
            return False
        
        # Fix the path
        if "window.location.href = '../dashboard.html';" in content:
            content = content.replace(
                "window.location.href = '../dashboard.html';",
                "window.location.href = 'dashboard.html';"
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed: {os.path.basename(filepath)}")
            return True
        else:
            print(f"✗ Pattern not found: {os.path.basename(filepath)}")
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
    
    print("\n🔄 Fixing dashboard links...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_dashboard_link(filepath):
                total_fixed += 1
    
    print(f"\n✅ Complete! Fixed {total_fixed} files.\n")

if __name__ == '__main__':
    main()
