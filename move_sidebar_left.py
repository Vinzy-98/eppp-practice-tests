#!/usr/bin/env python3
"""
Revert container changes and move sidebar to LEFT side instead
"""
import os
import glob

def fix_sidebar_position(filepath):
    """Move sidebar to left and restore container"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Restore container to original
        old_container = """        .container {
            max-width: calc(100% - 180px);
            margin: 0 auto;
            margin-right: 160px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        @media (min-width: 1200px) {
            .container {
                max-width: 900px;
            }
        }"""
        
        new_container = """        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }"""
        
        if old_container in content:
            content = content.replace(old_container, new_container)
            changes.append('Restored container')
        
        # 2. Move sidebar from RIGHT to LEFT
        old_sidebar = """        .review-summary {
            position: fixed;
            right: 20px;
            top: 100px;
            width: 120px;"""
        
        new_sidebar = """        .review-summary {
            position: fixed;
            left: 20px;
            top: 100px;
            width: 120px;"""
        
        if old_sidebar in content:
            content = content.replace(old_sidebar, new_sidebar)
            changes.append('Moved sidebar to LEFT')
        
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}: {', '.join(changes)}")
            return True
        else:
            print(f"⚠ No changes: {os.path.basename(filepath)}")
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
    
    print("\n🔄 Moving sidebar to LEFT and restoring container...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_sidebar_position(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
