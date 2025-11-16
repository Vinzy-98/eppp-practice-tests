#!/usr/bin/env python3
"""
Add resume functionality and time tracking to all test files
"""
import os
import re
import glob

def add_resume_and_time_tracking(filepath):
    """Add resume functionality and time tracking to a test file"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has resume functionality
        if 'saveProgress' in content and 'loadProgress' in content:
            print(f"✓ Already updated: {os.path.basename(filepath)}")
            return False
        
        # Add time tracking and resume functionality after the "let answersChecked = false;" line
        resume_code = """
        // Time tracking
        let testStartTime = Date.now();
        let testElapsedTime = 0;
        
        // Resume functionality
        function saveProgress() {
            if (answersChecked) return; // Don't save after test is submitted
            
            const testName = document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : 'Unknown Test';
            const questions = document.querySelectorAll('.question');
            const totalQuestions = questions.length;
            const answeredCount = document.querySelectorAll('.question.answered').length;
            
            // Collect all selected answers
            const answers = {};
            questions.forEach((q, index) => {
                const selected = q.querySelector('input[type="radio"]:checked');
                if (selected) {
                    answers[index] = selected.value;
                }
            });
            
            const progressData = {
                testName: testName,
                answers: answers,
                startTime: testStartTime,
                elapsedTime: Date.now() - testStartTime,
                totalQuestions: totalQuestions,
                answeredCount: answeredCount,
                savedAt: new Date().toISOString()
            };
            
            const user = JSON.parse(localStorage.getItem('eppp_user') || '{}');
            if (user.email) {
                const progressKey = `eppp_progress_${user.email}_${testName.replace(/\\\\s+/g, '_')}`;
                localStorage.setItem(progressKey, JSON.stringify(progressData));
            }
        }
        
        function loadProgress() {
            const testName = document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : 'Unknown Test';
            const user = JSON.parse(localStorage.getItem('eppp_user') || '{}');
            
            if (user.email) {
                const progressKey = `eppp_progress_${user.email}_${testName.replace(/\\\\s+/g, '_')}`;
                const savedProgress = localStorage.getItem(progressKey);
                
                if (savedProgress) {
                    const progress = JSON.parse(savedProgress);
                    
                    // Ask user if they want to resume
                    const resume = confirm(
                        `Resume previous attempt?\\\\n\\\\n` +
                        `Progress: ${progress.answeredCount}/${progress.totalQuestions} questions answered\\\\n` +
                        `Saved: ${new Date(progress.savedAt).toLocaleString()}\\\\n\\\\n` +
                        `Click OK to resume, or Cancel to start fresh.`
                    );
                    
                    if (resume) {
                        // Restore answers
                        const questions = document.querySelectorAll('.question');
                        Object.keys(progress.answers).forEach(index => {
                            const question = questions[parseInt(index)];
                            const answer = progress.answers[index];
                            const radio = question.querySelector(`input[value="${answer}"]`);
                            if (radio) {
                                radio.checked = true;
                                const choice = radio.closest('.choice');
                                choice.classList.add('selected');
                                question.classList.add('answered');
                            }
                        });
                        
                        // Restore time
                        testStartTime = progress.startTime || Date.now();
                        testElapsedTime = progress.elapsedTime || 0;
                        
                        // Update progress bar
                        updateProgress();
                        
                        return true;
                    } else {
                        // Clear saved progress if starting fresh
                        localStorage.removeItem(progressKey);
                    }
                }
            }
            return false;
        }
        
        function clearProgress() {
            const testName = document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : 'Unknown Test';
            const user = JSON.parse(localStorage.getItem('eppp_user') || '{}');
            
            if (user.email) {
                const progressKey = `eppp_progress_${user.email}_${testName.replace(/\\\\s+/g, '_')}`;
                localStorage.removeItem(progressKey);
            }
        }
"""
        
        # Find and replace the "let answersChecked = false;" line
        pattern = r'(let\s+answersChecked\s*=\s*false;)'
        if not re.search(pattern, content):
            print(f"✗ Could not find 'let answersChecked' line: {os.path.basename(filepath)}")
            return False
        
        content = re.sub(pattern, r'\1\n' + resume_code, content, count=1)
        
        # Modify selectChoice to auto-save
        old_select = r'(function selectChoice\(choiceElement\) \{[\s\S]+?updateProgress\(\);)'
        new_select = r'\1\n            saveProgress();'
        content = re.sub(old_select, new_select, content)
        
        # Modify checkAnswers to clear progress and save completion time
        old_check = r'(function checkAnswers\(\) \{)'
        new_check = r'\1\n            clearProgress();\n            const completionTime = Math.floor((Date.now() - testStartTime + testElapsedTime) / 1000);'
        content = re.sub(old_check, new_check, content)
        
        # Add completion time to results - use raw string replacement
        old_results = "document.getElementById('scoreDetails').innerHTML = \n                `Correct: ${correct} | Incorrect: ${incorrect} | Unanswered: ${unanswered}<br>Total: ${totalQuestions} questions`;"
        new_results = "document.getElementById('scoreDetails').innerHTML = \n                `Correct: ${correct} | Incorrect: ${incorrect} | Unanswered: ${unanswered}<br>Total: ${totalQuestions} questions<br>Time: ${Math.floor(completionTime / 60)}m ${completionTime % 60}s`;"
        content = content.replace(old_results, new_results)
        
        # Add load progress call at the end of script
        load_call = """
        // Load saved progress on page load
        window.addEventListener('DOMContentLoaded', function() {
            loadProgress();
        });
"""
        
        # Insert before closing script tag
        content = content.replace('</script>', load_call + '    </script>', 1)
        
        # Save the modified content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    # Get all test files
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Adding resume functionality and time tracking...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_resume_and_time_tracking(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
