#!/usr/bin/env python3
"""
Make review sidebar narrower - single column instead of 3
"""
import os
import glob

def narrow_review_sidebar(filepath):
    """Make the sidebar narrower with single column"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Reduce sidebar width from 250px to 120px
        old_width = """        .review-summary {
            position: fixed;
            right: 20px;
            top: 100px;
            width: 250px;"""
        
        new_width = """        .review-summary {
            position: fixed;
            right: 20px;
            top: 100px;
            width: 120px;"""
        
        if old_width in content:
            content = content.replace(old_width, new_width)
            changes.append('Reduced width to 120px')
        
        # 2. Change from 3 columns to 1 column
        old_grid = """        .review-links {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-top: 5px;
            padding: 5px;
        }"""
        
        new_grid = """        .review-links {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-top: 5px;
            padding: 5px;
        }"""
        
        if old_grid in content:
            content = content.replace(old_grid, new_grid)
            changes.append('Changed to single column')
        
        # 3. Adjust button padding for narrower width
        old_button = """        .review-link {
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
        
        new_button = """        .review-link {
            background: #f39c12;
            color: white;
            padding: 8px 10px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.2s;
            text-align: center;
            font-size: 0.85em;
            display: block;
        }"""
        
        if old_button in content:
            content = content.replace(old_button, new_button)
            changes.append('Adjusted button styling')
        
        # 4. Make heading smaller for narrow sidebar
        old_heading = """        .review-summary h3 {
            color: #856404;
            margin-bottom: 10px;
            font-size: 1em;
            position: sticky;
            top: 0;
            background: #fff3cd;
            padding: 5px 0;
            margin-top: -5px;
        }"""
        
        new_heading = """        .review-summary h3 {
            color: #856404;
            margin-bottom: 8px;
            font-size: 0.85em;
            position: sticky;
            top: 0;
            background: #fff3cd;
            padding: 5px 0;
            margin-top: -5px;
            text-align: center;
        }"""
        
        if old_heading in content:
            content = content.replace(old_heading, new_heading)
            changes.append('Smaller heading')
        
        # 5. Update mobile breakpoint to use single column too
        old_mobile = """        @media (max-width: 768px) {
            .review-summary {
                position: static;
                width: 100%;
                margin: 20px 0;
                max-height: 200px;
            }
            
            .review-links {
                grid-template-columns: repeat(5, 1fr);
            }
        }"""
        
        new_mobile = """        @media (max-width: 768px) {
            .review-summary {
                position: static;
                width: 100%;
                margin: 20px 0;
                max-height: 200px;
            }
            
            .review-links {
                flex-direction: row;
                flex-wrap: wrap;
            }
            
            .review-link {
                flex: 0 0 auto;
                min-width: 50px;
            }
        }"""
        
        if old_mobile in content:
            content = content.replace(old_mobile, new_mobile)
            changes.append('Updated mobile layout')
        
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
    
    print("\n🔄 Making review sidebar narrower...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if narrow_review_sidebar(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
