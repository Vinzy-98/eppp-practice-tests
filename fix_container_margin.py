#!/usr/bin/env python3
"""
Add margin-right to container to make room for sidebar
"""
import os
import glob

def add_container_margin(filepath):
    """Add margin to container for sidebar clearance"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update the .container CSS
        old_container = """        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }"""
        
        new_container = """        .container {
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
        
        if old_container in content:
            content = content.replace(old_container, new_container)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Added container margin: {os.path.basename(filepath)}")
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
    
    print("\n🔄 Adding container margin for sidebar...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_container_margin(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
