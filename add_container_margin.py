#!/usr/bin/env python3
"""
Add max-width to container to make room for the sidebar
"""
import os
import glob

def add_container_max_width(filepath):
    """Add max-width to container to avoid sidebar overlap"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # Find and update the .container CSS
        old_container = """        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }"""
        
        new_container = """        .container {
            max-width: calc(100% - 180px);
            margin: 0 auto;
            margin-right: 160px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        @media (min-width: 1200px) {
            .container {
                max-width: 900px;
            }
        }"""
        
        if old_container in content:
            content = content.replace(old_container, new_container)
            changes.append('Added container margin for sidebar')
        
        # Also update mobile media query to reset container on small screens
        old_mobile_media = """        @media (max-width: 768px) {
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
        
        new_mobile_media = """        @media (max-width: 768px) {
            .container {
                max-width: 100%;
                margin-right: auto;
            }
            
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
        
        if old_mobile_media in content:
            content = content.replace(old_mobile_media, new_mobile_media)
            changes.append('Updated mobile container')
        
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
    
    print("\n🔄 Adding container max-width for sidebar clearance...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_container_max_width(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
