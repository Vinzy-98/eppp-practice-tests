#!/usr/bin/env python3
"""
Add authentication check to all test HTML files
"""
import os
import glob

def add_auth_check(filepath):
    """Add authentication check to an HTML file if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if auth check already exists
        if 'eppp_authenticated' in content:
            print(f"✓ Already protected: {os.path.basename(filepath)}")
            return False
        
        # Find the <head> tag and add auth check after it
        auth_script = """<script>
        // Check authentication before loading page
        if (!sessionStorage.getItem('eppp_authenticated')) {
            window.location.href = '../login.html';
        }
    </script>
    """
        
        # For files in root directory
        if '/EPPP_Format/' not in filepath:
            auth_script = """<script>
        // Check authentication before loading page
        if (!sessionStorage.getItem('eppp_authenticated')) {
            window.location.href = 'login.html';
        }
    </script>
    """
        
        # Insert after <head> tag
        if '<head>' in content:
            content = content.replace('<head>', f'<head>\n    {auth_script}', 1)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Protected: {os.path.basename(filepath)}")
            return True
        else:
            print(f"✗ No <head> tag found: {os.path.basename(filepath)}")
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
        'EPPP_Format/AR_Exam_*_EPPP.html',
        'EPPP_Format/Practice_EPPP_*_EPPP.html'
    ]
    
    total_protected = 0
    
    print("\n🔒 Adding authentication to test files...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_auth_check(filepath):
                total_protected += 1
    
    print(f"\n✅ Complete! Protected {total_protected} files.\n")

if __name__ == '__main__':
    main()
