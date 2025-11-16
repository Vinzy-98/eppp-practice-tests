#!/usr/bin/env python3
"""
Add saveTestResults function and call to all test files
"""
import os
import glob
import re

def add_save_results_functionality(filepath):
    """Add saveTestResults function to test file"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has saveTestResults function
        if 'function saveTestResults(' in content:
            print(f"✓ Already has saveTestResults: {os.path.basename(filepath)}")
            return False
        
        # Step 1: Add call to saveTestResults in checkAnswers
        pattern1 = r"(document\.getElementById\('resultsSummary'\)\.classList\.add\('show'\);)\s*\n\s*\n\s*(// Disable check button)"
        replacement1 = r"\1\n            \n            // Save test results\n            saveTestResults(correct, incorrect, unanswered, totalQuestions, percentage, completionTime);\n            \n            \2"
        
        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
        else:
            print(f"✗ Could not find insertion point for saveTestResults call: {os.path.basename(filepath)}")
            return False
        
        # Step 2: Add saveTestResults function definition
        save_function = """        
        function saveTestResults(correct, incorrect, unanswered, totalQuestions, percentage, completionTime) {
            if (!currentUser) {
                console.warn('No user logged in, results not saved');
                return;
            }
            
            const examTitle = document.querySelector('.exam-title').textContent;
            const historyKey = 'eppp_history_' + currentUser.name.replace(/\\\\s+/g, '_');
            const history = JSON.parse(localStorage.getItem(historyKey) || '[]');
            
            const testResult = {
                test: examTitle,
                score: percentage,
                correct: correct,
                incorrect: incorrect,
                unanswered: unanswered,
                totalQuestions: totalQuestions,
                completionTime: completionTime,
                date: new Date().toISOString(),
                attemptNumber: currentAttempt
            };
            
            history.push(testResult);
            localStorage.setItem(historyKey, JSON.stringify(history));
            
            // Also save in new format for dashboard compatibility
            const userTestsKey = `eppp_user_${currentUser.email || currentUser.name}_tests`;
            const userTests = JSON.parse(localStorage.getItem(userTestsKey) || '[]');
            
            const testResultNew = {
                testName: examTitle,
                score: percentage,
                correct: correct,
                incorrect: incorrect,
                unanswered: unanswered,
                totalQuestions: totalQuestions,
                completedAt: new Date().toISOString(),
                attemptNumber: currentAttempt
            };
            
            userTests.push(testResultNew);
            localStorage.setItem(userTestsKey, JSON.stringify(userTests));
            
            console.log('Test results saved successfully!');
        }
"""
        
        # Insert before resetTest function
        pattern2 = r"(\n\s+function resetTest\(\) \{)"
        if re.search(pattern2, content):
            content = re.sub(pattern2, save_function + r'\1', content, count=1)
        else:
            print(f"✗ Could not find resetTest function: {os.path.basename(filepath)}")
            return False
        
        # Save the modified content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added saveTestResults: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    # Get all test files
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    total_updated = 0
    
    print("\n🔄 Adding saveTestResults functionality...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if add_save_results_functionality(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
