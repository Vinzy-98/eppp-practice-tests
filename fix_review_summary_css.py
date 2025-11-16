#!/usr/bin/env python3
"""
Fix review summary CSS to prevent it from expanding uncontrollably
"""
import os
import glob
import re

def fix_review_summary_css(filepath):
    """Fix the review summary CSS"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the review-summary CSS
        old_css = """        .review-summary {
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
            display: none;
        }"""
        
        new_css = """        .review-summary {
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
            display: none;
            max-width: 100%;
            overflow: hidden;
        }"""
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            
            # Also improve the review-links container
            old_links_css = """        .review-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }"""
            
            new_links_css = """        .review-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
            max-width: 100%;
            overflow-x: auto;
            max-height: 200px;
            overflow-y: auto;
            padding: 5px;
        }"""
            
            if old_links_css in content:
                content = content.replace(old_links_css, new_links_css)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed review summary CSS: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠ Pattern not found: {os.path.basename(filepath)}")
            return False
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Fixing review summary CSS...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_review_summary_css(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Fixed {total_updated} files.\n")

if __name__ == '__main__':
    main()
