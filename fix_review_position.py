#!/usr/bin/env python3
"""
Move review-summary div outside button-container and increase z-index
"""
import os
import glob
import re

def fix_review_position(filepath):
    """Move review div and fix z-index"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Increase z-index in CSS to be above everything
        old_z = """            z-index: 100;
            max-height: calc(100vh - 120px);"""
        
        new_z = """            z-index: 1000;
            max-height: calc(100vh - 120px);"""
        
        if old_z in content:
            content = content.replace(old_z, new_z)
            changes.append('Increased z-index')
        
        # 2. Move the review-summary div out of button-container
        # Find the current position (inside button-container)
        pattern = r'(<div class="button-container">.*?<div class="progress-fill" id="progressBar">0%</div>\s*</div>\s*)(<div class="review-summary" id="reviewSummary">.*?</div>)(.*?<button onclick="checkAnswers\(\)")'
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # Reconstruct: progress bar, then buttons, then review-summary after button-container closes
            before_review = match.group(1)
            review_div = match.group(2)
            after_review = match.group(3)
            
            # Remove review from its current location and place it after button-container closes
            # Find the closing of button-container
            button_container_pattern = r'(<div class="button-container">.*?<div class="progress-fill" id="progressBar">0%</div>\s*</div>)\s*<div class="review-summary".*?</div>(.*?</div>)\s*(<div class="results-summary")'
            
            button_match = re.search(button_container_pattern, content, re.DOTALL)
            if button_match:
                progress_section = button_match.group(1)
                buttons_and_close = button_match.group(2)
                results_section = button_match.group(3)
                
                # Reconstruct with review-summary AFTER button-container closes
                new_structure = progress_section + '\n\n            ' + buttons_and_close.strip() + '\n        </div>\n\n        <div class="review-summary" id="reviewSummary">\n            <h3>📋 Questions Marked for Review</h3>\n            <div class="review-links" id="reviewLinks"></div>\n        </div>\n\n        ' + results_section
                
                content = re.sub(button_container_pattern, new_structure, content, count=1, flags=re.DOTALL)
                changes.append('Moved div outside container')
        
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
    
    print("\n🔄 Fixing review summary position...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if fix_review_position(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Fixed {total_updated} files.\n")

if __name__ == '__main__':
    main()
