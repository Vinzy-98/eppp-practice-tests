#!/usr/bin/env python3
"""
Move review summary to a fixed sidebar on the right
"""
import os
import glob
import re

def move_review_to_sidebar(filepath):
    """Convert review summary to a fixed sidebar"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Update CSS for review-summary to be a fixed sidebar
        old_summary_css = """        .review-summary {
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
            display: none;
            max-width: 100%;
            overflow: hidden;
        }"""
        
        new_summary_css = """        .review-summary {
            position: fixed;
            right: 20px;
            top: 100px;
            width: 250px;
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            display: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 100;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }"""
        
        if old_summary_css in content:
            content = content.replace(old_summary_css, new_summary_css)
            changes.append('Sidebar CSS')
        
        # 2. Update review-summary h3 to be smaller
        old_h3_css = """        .review-summary h3 {
            color: #856404;
            margin-bottom: 10px;
        }"""
        
        new_h3_css = """        .review-summary h3 {
            color: #856404;
            margin-bottom: 10px;
            font-size: 1em;
            position: sticky;
            top: 0;
            background: #fff3cd;
            padding: 5px 0;
            margin-top: -5px;
        }"""
        
        if old_h3_css in content:
            content = content.replace(old_h3_css, new_h3_css)
            changes.append('Heading CSS')
        
        # 3. Update review-links to work better in sidebar
        old_links_css = """        .review-links {
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
        
        new_links_css = """        .review-links {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-top: 5px;
            padding: 5px;
        }"""
        
        if old_links_css in content:
            content = content.replace(old_links_css, new_links_css)
            changes.append('Links layout')
        
        # 4. Update review-link button styling for smaller sidebar
        old_link_css = """        .review-link {
            background: #f39c12;
            color: white;
            padding: 6px 12px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.2s;
        }"""
        
        new_link_css = """        .review-link {
            background: #f39c12;
            color: white;
            padding: 8px 4px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.2s;
            text-align: center;
            font-size: 0.9em;
        }"""
        
        if old_link_css in content:
            content = content.replace(old_link_css, new_link_css)
            changes.append('Link buttons')
        
        # 5. Add media query for mobile responsiveness
        old_style_close = """        .review-link:hover {
            background: #e67e22;
            transform: translateY(-2px);
        }
        </style>"""
        
        new_style_close = """        .review-link:hover {
            background: #e67e22;
            transform: translateY(-2px);
        }
        
        @media (max-width: 768px) {
            .review-summary {
                position: static;
                width: 100%;
                margin: 20px 0;
                max-height: 200px;
            }
            
            .review-links {
                grid-template-columns: repeat(5, 1fr);
            }
        }
        </style>"""
        
        if old_style_close in content:
            content = content.replace(old_style_close, new_style_close)
            changes.append('Mobile responsive')
        
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}: {', '.join(changes)}")
            return True
        else:
            print(f"⚠ No changes in: {os.path.basename(filepath)}")
            return False
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Moving review summary to sidebar...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if move_review_to_sidebar(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
