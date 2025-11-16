#!/usr/bin/env python3
"""
Create proper two-column layout: sidebar left, content right
"""
import os
import glob

def create_two_column_layout(filepath):
    """Create two-column layout with sidebar and content"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Update body to use flexbox
        old_body = """        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }"""
        
        new_body = """        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
        }"""
        
        if old_body in content:
            content = content.replace(old_body, new_body)
            changes.append('Updated body flexbox')
        
        # 2. Update review-summary to be a column
        old_sidebar = """        .review-summary {
            position: fixed;
            left: 20px;
            top: 100px;
            width: 120px;
            background: #fff3cd;
            border: 2px solid #f39c12;
            border-radius: 8px;
            padding: 15px;
            display: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }"""
        
        new_sidebar = """        .review-summary {
            position: fixed;
            left: 0;
            top: 0;
            width: 150px;
            height: 100vh;
            background: #fff3cd;
            border-right: 3px solid #f39c12;
            padding: 20px 15px;
            display: none;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            z-index: 1000;
            overflow-y: auto;
        }"""
        
        if old_sidebar in content:
            content = content.replace(old_sidebar, new_sidebar)
            changes.append('Sidebar full-height column')
        
        # 3. Update container to account for sidebar
        old_container = """        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }"""
        
        new_container = """        .container {
            max-width: 900px;
            margin: 20px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            flex: 1;
        }
        
        body.has-sidebar .container {
            margin-left: 170px;
        }"""
        
        if old_container in content:
            content = content.replace(old_container, new_container)
            changes.append('Container with sidebar margin')
        
        # 4. Update the updateReviewSummary function to add body class
        old_function = """        function updateReviewSummary() {
            const markedQuestions = document.querySelectorAll('.question.marked-review');
            const summary = document.getElementById('reviewSummary');
            const linksContainer = document.getElementById('reviewLinks');
            
            if (markedQuestions.length > 0) {
                summary.classList.add('show');
                linksContainer.innerHTML = '';"""
        
        new_function = """        function updateReviewSummary() {
            const markedQuestions = document.querySelectorAll('.question.marked-review');
            const summary = document.getElementById('reviewSummary');
            const linksContainer = document.getElementById('reviewLinks');
            
            if (markedQuestions.length > 0) {
                summary.classList.add('show');
                document.body.classList.add('has-sidebar');
                linksContainer.innerHTML = '';"""
        
        if old_function in content:
            content = content.replace(old_function, new_function)
            changes.append('Add body class on show')
        
        # 5. Update to remove body class when no marked questions
        old_hide = """            } else {
                summary.classList.remove('show');
            }
        }"""
        
        new_hide = """            } else {
                summary.classList.remove('show');
                document.body.classList.remove('has-sidebar');
            }
        }"""
        
        if old_hide in content:
            content = content.replace(old_hide, new_hide)
            changes.append('Remove body class on hide')
        
        # 6. Update mobile to reset body
        old_mobile = """        @media (max-width: 768px) {
            .container {
                max-width: 100%;
                margin-right: auto;
            }
            
            .review-summary {
                position: static;
                width: 100%;
                margin: 20px 0;
                max-height: 200px;
            }"""
        
        new_mobile = """        @media (max-width: 768px) {
            body {
                display: block;
                padding: 20px;
            }
            
            body.has-sidebar .container {
                margin-left: auto;
            }
            
            .container {
                margin: 0 auto;
            }
            
            .review-summary {
                position: static;
                width: 100%;
                height: auto;
                margin: 20px 0;
                max-height: 200px;
                border-right: none;
                border: 2px solid #f39c12;
                border-radius: 8px;
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
    
    print("\n🔄 Creating two-column layout...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if create_two_column_layout(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
