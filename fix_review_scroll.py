#!/usr/bin/env python3
"""
Fix review links to actually scroll instead of expanding
"""
import os
import glob

def fix_review_links_scroll(filepath):
    """Fix the review links container to scroll properly"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the review-links CSS completely
        old_css = """        .review-links {
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
        
        new_css = """        .review-links {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
            gap: 10px;
            margin-top: 10px;
            max-height: 150px;
            overflow-y: auto;
            overflow-x: hidden;
            padding: 5px;
            border: 1px solid #f39c12;
            border-radius: 4px;
            background: #fffbf0;
        }"""
        
        if old_css in content:
            content = content.replace(old_css, new_css)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed review links scroll: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠ Pattern not found in: {os.path.basename(filepath)}")
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
    
    print("\n🔄 Fixing review links scrolling...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_review_links_scroll(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Fixed {total_updated} files.\n")

if __name__ == '__main__':
    main()
