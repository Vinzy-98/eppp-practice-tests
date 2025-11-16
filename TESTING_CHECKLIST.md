# EPPP Manual Testing Checklist

## ⚠️ IMPORTANT: Test Everything Before Using

This checklist verifies that all critical functionality works correctly. **Test these in order.**

---

## Prerequisites
- Use Chrome, Safari, or Firefox
- Clear browser cache if testing after updates
- Have at least 10 minutes to complete all tests

---

## Test 1: Authentication ✓
**Purpose:** Verify login system works

1. Navigate to: https://vinzy-98.github.io/eppp-practice-tests/
2. You should see a login page
3. Enter password: `EPPP2025`
4. Click "Access Tests"
5. **Expected:** You are redirected to the main page

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 2: User Registration ✓
**Purpose:** Verify user tracking works

1. Click on any test (e.g., "AR Exam 1")
2. A modal should appear asking for your name
3. Enter: Name: `Test User`, Email: `test@example.com`
4. Click "Start Test"
5. **Expected:** Modal closes, you see the test questions

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 3: Taking a Test ✓
**Purpose:** Verify basic test functionality

1. Answer at least 5 questions (select any answers)
2. Check the progress bar updates (should show "5 of X questions answered")
3. Scroll down and click "Check Answers"
4. **Expected:** 
   - Results appear at top showing your score
   - Each question shows ✓ or ✗
   - Correct answers are highlighted in green
   - "Download Results" button appears

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 4: Saving Results ✓
**Purpose:** Verify results are saved to localStorage

1. After completing Test 3, open browser DevTools (F12 or Cmd+Option+I)
2. Go to "Application" or "Storage" tab → Local Storage
3. Look for keys starting with `eppp_`
4. **Expected:** You should see:
   - `eppp_user` - your user info
   - `eppp_history_Test_User` - test history (old format)
   - `eppp_user_test@example.com_tests` - test results (new format)

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 5: Download Results ✓
**Purpose:** Verify download functionality

1. After checking answers in Test 3, click "Download Results"
2. **Expected:** A .txt file downloads
3. Open the file
4. **Expected:** File contains:
   - Test title
   - Your score
   - Detailed results for each question
   - Your answer vs correct answer
   - Completion timestamp

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 6: Dashboard Display ✓
**Purpose:** Verify dashboard shows test history

1. Click "📊 My Dashboard" button (top right)
2. **Expected:** Dashboard shows:
   - Your name and email
   - Stats cards (Total Attempts, Average Score, etc.)
   - Charts showing your progress
   - List of all completed tests with scores
   - Each test shows: name, score, date, attempt number

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 7: Resume Functionality ✓
**Purpose:** Verify tests can be paused and resumed

1. Start a NEW test (different from Test 3)
2. Answer 3-5 questions (don't complete the test)
3. **Don't click "Check Answers"**
4. Close the browser tab/window
5. Navigate back to the same test
6. **Expected:** You see a prompt: "You have a saved session..."
7. Click "Resume"
8. **Expected:** Your previous answers are restored

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 8: Mark for Review ✓
**Purpose:** Verify review marking works

1. In any test, click the "🔖 Mark for Review" button below a question
2. **Expected:** 
   - Button turns green and says "✓ Marked for Review"
   - Question background becomes yellow/orange
3. Mark 2-3 questions
4. **Expected:** A summary box appears at top showing "Questions Marked for Review"
5. Click on a question number in the summary (e.g., "Q5")
6. **Expected:** Page scrolls to that question

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 9: Incomplete Tests on Dashboard ✓
**Purpose:** Verify dashboard shows in-progress tests

1. Start a test, answer a few questions, then leave (don't complete)
2. Go to Dashboard
3. Scroll to "In-Progress Tests" section
4. **Expected:** Shows the test you started with:
   - Test name
   - Progress (e.g., "5 of 100 questions answered")
   - Progress bar
   - "Resume Test" and "Clear Progress" buttons

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 10: Export/Import Progress ✓
**Purpose:** Verify data portability

### Export:
1. Go to Dashboard
2. Click "Export Progress" button
3. **Expected:** A .eppp file downloads

### Import:
4. Open the downloaded .eppp file in a text editor
5. Verify it's valid JSON with your test data
6. On Dashboard, click "Import Progress"
7. Select the .eppp file you downloaded
8. **Expected:** Success message appears

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 11: Multiple Attempts ✓
**Purpose:** Verify attempt tracking

1. Complete the same test twice (reset and retake)
2. Go to Dashboard
3. **Expected:** Both attempts appear in the history
4. Each attempt shows "Attempt #1", "Attempt #2", etc.

**Status:** □ Pass □ Fail
**Notes:**

---

## Test 12: Cross-Device Compatibility ✓
**Purpose:** Verify export/import allows device switching

1. Export progress on Device A (see Test 10)
2. Email the .eppp file to yourself
3. Open on Device B
4. Navigate to Dashboard and import the file
5. **Expected:** All your progress appears on Device B

**Status:** □ Pass □ Fail
**Notes:**

---

## Common Issues & Fixes

### Issue: "Nothing is saving"
**Fix:** 
- Check if you entered your name when starting the test
- Verify localStorage is enabled (check DevTools → Application → Local Storage)
- Make sure you clicked "Check Answers" to complete the test

### Issue: "Dashboard is empty"
**Fix:**
- Complete at least one test first
- Check localStorage has `eppp_history_` and `eppp_user_*_tests` keys
- Hard refresh the dashboard (Ctrl+F5 or Cmd+Shift+R)

### Issue: "Download not working"
**Fix:**
- Make sure you clicked "Check Answers" first
- Check if downloads are blocked in browser settings
- Try a different browser

### Issue: "Resume not working"
**Fix:**
- Make sure you left the test without clicking "Check Answers"
- Check localStorage for `eppp_progress_` keys
- Clear browser cache and try again

### Issue: "404 error on dashboard"
**Fix:**
- This should be fixed in latest version
- Make sure you're using the deployed version at: https://vinzy-98.github.io/eppp-practice-tests/
- Not a local file:// URL

---

## Automated Test Page

For quick verification, open:
`test_functionality.html`

This page has buttons to test each function programmatically.

---

## Browser DevTools Checks

### Check localStorage:
1. Open DevTools (F12)
2. Application/Storage → Local Storage
3. Should see keys:
   - `eppp_user`
   - `eppp_history_{username}`
   - `eppp_user_{email}_tests`
   - `eppp_progress_{email}_{testname}` (for incomplete tests)

### Check for JavaScript errors:
1. Open DevTools (F12)
2. Go to Console tab
3. Complete a test
4. **Expected:** No red errors (warnings are OK)

---

## Final Verification

After completing all tests:

□ All tests passed
□ No critical errors in console
□ localStorage contains correct data
□ Can export and import successfully
□ Dashboard displays all completed tests
□ Resume works for incomplete tests
□ Download produces valid files
□ Mark for review functions correctly

**Overall Status:** □ READY FOR USE □ NEEDS FIXES

**Date Tested:** _______________
**Browser:** _______________
**Notes:**
