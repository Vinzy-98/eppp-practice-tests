#!/usr/bin/env python3
"""
1. Enhance download to show full answer text (not just A/B/C/D)
2. Add "Back to Tests" navigation button
"""
import os
import glob
import re

def enhance_download_and_navigation(filepath):
    """Enhance download function and add navigation"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = []
        
        # 1. Enhance downloadResults to show full answer text
        old_download = """            const questions = document.querySelectorAll('.question');
            questions.forEach((question, index) => {
                const questionNum = question.dataset.question;
                const correctAnswer = question.dataset.correct;
                const questionText = question.querySelector('.question-text').textContent;
                const selectedRadio = question.querySelector('input[type="radio"]:checked');
                const selectedAnswer = selectedRadio ? selectedRadio.value : 'Not answered';
                
                const isCorrect = selectedAnswer === correctAnswer;
                const status = !selectedRadio ? '⚠️ NOT ANSWERED' : (isCorrect ? '✓ CORRECT' : '✗ INCORRECT');
                
                resultsText += `Question ${questionNum}:\\n`;
                resultsText += `${questionText}\\n\\n`;
                resultsText += `Your Answer: ${selectedAnswer}\\n`;
                resultsText += `Correct Answer: ${correctAnswer}\\n`;
                resultsText += `Status: ${status}\\n`;
                resultsText += `${'-'.repeat(50)}\\n\\n`;
            });"""
        
        new_download = """            const questions = document.querySelectorAll('.question');
            questions.forEach((question, index) => {
                const questionNum = question.dataset.question;
                const correctAnswer = question.dataset.correct;
                const questionText = question.querySelector('.question-text').textContent;
                const selectedRadio = question.querySelector('input[type="radio"]:checked');
                const selectedAnswer = selectedRadio ? selectedRadio.value : 'Not answered';
                
                // Get the full text of selected and correct answers
                let selectedAnswerText = selectedAnswer;
                let correctAnswerText = correctAnswer;
                
                if (selectedRadio) {
                    const selectedLabel = selectedRadio.nextElementSibling;
                    if (selectedLabel) {
                        selectedAnswerText = `${selectedAnswer}: ${selectedLabel.textContent.trim()}`;
                    }
                }
                
                const correctChoice = question.querySelector(`input[value="${correctAnswer}"]`);
                if (correctChoice && correctChoice.nextElementSibling) {
                    correctAnswerText = `${correctAnswer}: ${correctChoice.nextElementSibling.textContent.trim()}`;
                }
                
                const isCorrect = selectedAnswer === correctAnswer;
                const status = !selectedRadio ? '⚠️ NOT ANSWERED' : (isCorrect ? '✓ CORRECT' : '✗ INCORRECT');
                
                resultsText += `Question ${questionNum}:\\n`;
                resultsText += `${questionText}\\n\\n`;
                resultsText += `Your Answer: ${selectedAnswerText}\\n`;
                resultsText += `Correct Answer: ${correctAnswerText}\\n`;
                resultsText += `Status: ${status}\\n`;
                resultsText += `${'-'.repeat(50)}\\n\\n`;
            });"""
        
        if old_download in content:
            content = content.replace(old_download, new_download)
            changes.append('Enhanced download')
        
        # 2. Add "Back to Tests" button after dashboard button
        # Find the user panel div with dashboard button
        old_nav = """            <button class="dashboard-btn" onclick="openDashboard()">📊 My Dashboard</button>
        </div>"""
        
        new_nav = """            <button class="dashboard-btn" onclick="openDashboard()">📊 My Dashboard</button>
            <button class="dashboard-btn" onclick="window.location.href='tests.html'" style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);">📚 All Tests</button>
        </div>"""
        
        if old_nav in content and new_nav not in content:
            content = content.replace(old_nav, new_nav)
            changes.append('Added navigation button')
        
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}: {', '.join(changes)}")
            return True
        else:
            print(f"⚠ {os.path.basename(filepath)}: No changes needed")
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
    
    print("\n🔄 Enhancing download and navigation...\n")
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            if enhance_download_and_navigation(filepath):
                total_updated += 1
    
    print(f"\n✅ Complete! Updated {total_updated} files.\n")

if __name__ == '__main__':
    main()
