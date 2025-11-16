#!/usr/bin/env python3
"""
Automated verification of critical EPPP functionality
This script checks that all the key functions exist in the test files
"""
import os
import re
import glob

def check_file(filepath):
    """Check a single test file for required functions"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    issues = []
    checks = []
    
    # Check 1: User registration functions
    if 'function initializeUser(' in content or 'function saveUserInfo(' in content:
        checks.append('✓ User registration')
    else:
        issues.append('✗ Missing user registration functions')
    
    # Check 2: Save results function
    if 'function saveTestResults(' in content:
        checks.append('✓ Save test results')
    else:
        issues.append('✗ Missing saveTestResults function')
    
    # Check 3: Both storage formats
    if 'eppp_history_' in content and 'eppp_user_' in content:
        checks.append('✓ Both storage formats')
    else:
        issues.append('✗ Missing storage format keys')
    
    # Check 4: Resume functionality
    if 'function loadProgress(' in content and 'function saveProgress(' in content:
        checks.append('✓ Resume functions')
        # Check if loadProgress is called
        if 'loadProgress();' in content:
            checks.append('✓ loadProgress() called')
        else:
            issues.append('✗ loadProgress() defined but not called')
    else:
        issues.append('✗ Missing resume functions')
    
    # Check 5: Download results
    if 'function downloadResults(' in content:
        checks.append('✓ Download results')
        # Check if it uses innerHTML (not textContent)
        if "scoreDetails').innerHTML" in content:
            checks.append('✓ Download uses innerHTML')
        elif "scoreDetails').textContent" in content:
            issues.append('✗ Download still uses textContent (should be innerHTML)')
    else:
        issues.append('✗ Missing downloadResults function')
    
    # Check 6: Download button visibility
    if "downloadBtn').style.display = 'inline-block'" in content:
        checks.append('✓ Download button shown')
    else:
        issues.append('✗ Download button not shown after check')
    
    # Check 7: Mark for review
    if 'function toggleReview(' in content:
        checks.append('✓ Mark for review')
    else:
        issues.append('✗ Missing mark for review function')
    
    # Check 8: Check answers function
    if 'function checkAnswers(' in content:
        checks.append('✓ Check answers')
        # Verify it calls saveTestResults
        match = re.search(r'function checkAnswers\(\)[\s\S]{1,2000}saveTestResults\(', content)
        if match:
            checks.append('✓ checkAnswers calls saveTestResults')
        else:
            issues.append('✗ checkAnswers does not call saveTestResults')
    else:
        issues.append('✗ Missing checkAnswers function')
    
    # Check 9: Dashboard link
    if 'function openDashboard(' in content:
        if "dashboard.html'" in content and not "../dashboard.html" in content:
            checks.append('✓ Dashboard link correct')
        else:
            issues.append('✗ Dashboard link may be incorrect')
    
    return {
        'filename': filename,
        'checks': checks,
        'issues': issues,
        'status': 'PASS' if len(issues) == 0 else 'FAIL'
    }

def main():
    base_dir = "/Users/vagrawal/Documents/Personal/Dhriti - EPPP/Interactive_Tests"
    
    patterns = [
        'AR_Exam_*.html',
        'Practice_EPPP_*.html',
    ]
    
    print("\n" + "="*80)
    print("EPPP FUNCTIONALITY VERIFICATION")
    print("="*80 + "\n")
    
    all_results = []
    
    for pattern in patterns:
        files = glob.glob(os.path.join(base_dir, pattern))
        for filepath in sorted(files):
            result = check_file(filepath)
            all_results.append(result)
    
    # Print summary
    passed = sum(1 for r in all_results if r['status'] == 'PASS')
    failed = sum(1 for r in all_results if r['status'] == 'FAIL')
    
    print(f"📊 SUMMARY: {passed} passed, {failed} failed out of {len(all_results)} files\n")
    
    # Print details for failed tests
    if failed > 0:
        print("\n❌ FAILED FILES:\n")
        for result in all_results:
            if result['status'] == 'FAIL':
                print(f"\n{result['filename']}:")
                for issue in result['issues']:
                    print(f"  {issue}")
    
    # Print details for passed tests
    if passed > 0:
        print("\n✅ PASSED FILES:\n")
        for result in all_results:
            if result['status'] == 'PASS':
                print(f"  {result['filename']} - All checks passed")
    
    # Print detailed checks for first file
    if all_results:
        print("\n" + "="*80)
        print(f"DETAILED CHECKS FOR {all_results[0]['filename']}:")
        print("="*80)
        for check in all_results[0]['checks']:
            print(f"  {check}")
        if all_results[0]['issues']:
            print("\n  Issues:")
            for issue in all_results[0]['issues']:
                print(f"  {issue}")
    
    print("\n" + "="*80 + "\n")
    
    # Check dashboard
    print("CHECKING DASHBOARD:\n")
    dashboard_path = os.path.join(base_dir, 'dashboard.html')
    if os.path.exists(dashboard_path):
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
        
        dashboard_checks = []
        dashboard_issues = []
        
        if 'function loadDashboard(' in dashboard_content:
            dashboard_checks.append('✓ loadDashboard function exists')
        else:
            dashboard_issues.append('✗ Missing loadDashboard function')
        
        if 'eppp_history_' in dashboard_content and 'eppp_user_' in dashboard_content:
            dashboard_checks.append('✓ Both storage formats supported')
        else:
            dashboard_issues.append('✗ Missing storage format support')
        
        if 'function displayIncompleteTests(' in dashboard_content:
            dashboard_checks.append('✓ Incomplete tests display')
        else:
            dashboard_issues.append('✗ Missing incomplete tests function')
        
        if 'function exportProgress(' in dashboard_content:
            dashboard_checks.append('✓ Export function exists')
        else:
            dashboard_issues.append('✗ Missing export function')
        
        for check in dashboard_checks:
            print(f"  {check}")
        for issue in dashboard_issues:
            print(f"  {issue}")
        
        if dashboard_issues:
            print("\n  ❌ Dashboard has issues")
        else:
            print("\n  ✅ Dashboard passed all checks")
    
    print("\n" + "="*80)
    
    return failed == 0

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
