# Resume Feature Guide

## Overview
The EPPP Practice Tests platform now includes a powerful **Resume** feature that allows you to pause any test and continue it later—even on a different device!

## Key Features

### 1. **Automatic Progress Saving**
- Your answers are automatically saved after each question you answer
- No need to manually save—it happens in the background
- Progress is saved to your browser's local storage

### 2. **Resume Prompt**
When you return to a test with saved progress:
- You'll see a prompt asking if you want to resume
- Shows how many questions you've answered (e.g., "12 of 175 questions answered")
- Shows when the progress was saved
- **Click OK** to continue where you left off
- **Click Cancel** to start fresh (this will clear saved progress)

### 3. **Time Tracking**
- All tests now track how long you take to complete them
- Time is displayed in the results (e.g., "Time: 45m 32s")
- Time tracking continues even if you pause and resume
- Helps you practice time management for the actual EPPP exam

### 4. **Cross-Device Resume**
You can pause on one device and resume on another:

1. **Export your progress** from the Dashboard
   - Click "📤 Export Progress" button
   - Save the `.eppp` file to your device
   
2. **Email or transfer** the `.eppp` file to yourself
   - Send it via email, cloud storage, or any file transfer method
   
3. **Import on another device**
   - Open the Dashboard on your new device
   - Click "📥 Import Progress"
   - Select your `.eppp` file
   - Your incomplete tests will be restored!

### 5. **In-Progress Tests Dashboard**
The Dashboard now shows all your incomplete tests:
- **⏸️ In-Progress Tests** section appears when you have saved progress
- Shows each test with:
  - Progress bar (visual indicator)
  - Questions answered (e.g., "45 of 175 questions")
  - Time since last save (e.g., "2h ago")
  - **▶️ Resume Test** button to continue
  - **✕** button to clear saved progress

## How to Use

### Starting a Test
1. Select any test from the test browser
2. Begin answering questions
3. Your progress is automatically saved after each answer

### Pausing a Test
- Simply **close the browser tab** or **navigate away**
- Your progress is already saved—no action needed
- You can return anytime to resume

### Resuming a Test
**Method 1: Direct Link**
1. Go back to the same test
2. Click **OK** when prompted to resume

**Method 2: From Dashboard**
1. Go to your Dashboard
2. Find the test in "⏸️ In-Progress Tests"
3. Click **▶️ Resume Test**

### Clearing Progress
If you want to start a test fresh:
- **During resume prompt**: Click **Cancel**
- **From Dashboard**: Click the **✕** button next to the test

### Transferring Progress
**On Device A:**
1. Go to Dashboard
2. Click "📤 Export Progress"
3. Save the `.eppp` file
4. Email it to yourself or save to cloud storage

**On Device B:**
1. Download/retrieve the `.eppp` file
2. Go to Dashboard
3. Click "📥 Import Progress"
4. Select the file
5. Resume your test!

## Important Notes

### ✅ What's Saved
- All your selected answers
- Current question position
- Time spent so far
- Which questions you've answered

### ❌ What's NOT Saved
- Checked answers (after clicking "Check Answers")
- Results and scores (only completed tests are saved)
- Scrolling position on the page

### Browser Compatibility
- Works in all modern browsers:
  - ✅ Chrome / Edge / Brave
  - ✅ Firefox
  - ✅ Safari
  - ✅ Mobile browsers (iOS Safari, Chrome Mobile)

### Privacy & Storage
- Progress is stored **locally** in your browser
- No data is sent to any server
- Clearing browser data will **delete** saved progress
- **Export regularly** to prevent data loss!

## Troubleshooting

### "Resume prompt doesn't appear"
**Cause**: Progress might not have been saved or was cleared

**Solution**:
- Check if you answered any questions (progress only saves after answering)
- Try the "⏸️ In-Progress Tests" section in Dashboard
- Import your `.eppp` file if you have one

### "Progress shows wrong number of questions"
**Cause**: Test file may have been updated

**Solution**:
- Clear the saved progress and start fresh
- Click the **✕** button in Dashboard

### "Can't resume on another device"
**Cause**: Progress is stored locally per device

**Solution**:
- Use the Export/Import feature:
  1. Export from original device
  2. Import on new device
- This is the **only** way to transfer progress

### "Lost my progress after updating browser"
**Cause**: Browser updates usually preserve data, but not always

**Solution**:
- **Prevention**: Export your progress regularly
- If lost, you'll need to restart affected tests
- Set a reminder to export weekly if actively testing

### "Export file doesn't work"
**Cause**: File might be corrupted or wrong format

**Solution**:
- Ensure file has `.eppp` extension
- Don't edit the file manually
- Re-export from original device

## Tips for Best Experience

### 📤 Export Regularly
- Export progress **at least once per week**
- Keep backups of your `.eppp` files
- Name files with dates: `EPPP_Progress_2024-01-15.eppp`

### ⏸️ Use Resume Strategically
- Take breaks during long tests
- Split sessions to maintain focus
- Resume when you're fresh and alert

### ⏱️ Practice Time Management
- Monitor completion times in results
- Try to improve your pace over time
- The actual EPPP has strict time limits

### 🎯 Clear Old Progress
- Remove incomplete tests you don't plan to finish
- Keeps Dashboard clean and organized
- Click **✕** button in "In-Progress Tests" section

### 📱 Multi-Device Workflow
For maximum flexibility:
1. Start test on desktop
2. Export progress
3. Email `.eppp` file to yourself
4. Continue on tablet/phone during commute
5. Export again and finish on desktop

## Privacy & Security

### What's in the Export File?
Your `.eppp` file contains:
- Your name and email
- All completed test scores and dates
- All incomplete test progress
- Question answers (but not the questions themselves)
- Timestamps and statistics

### Is My Data Safe?
- ✅ No data sent to servers
- ✅ All storage is local
- ✅ Export files are encrypted JSON
- ⚠️ Export files contain personal data—store securely
- ⚠️ Don't share export files publicly

### Sharing Devices
If you share a computer:
- Consider using private/incognito mode
- Export and clear progress after each session
- Or use separate user accounts

## Examples

### Scenario 1: Daily Practice
**Monday (30 min available):**
1. Start Practice EPPP 1
2. Answer 50 questions
3. Close browser—progress auto-saved

**Tuesday (30 min available):**
1. Open Practice EPPP 1
2. Click "OK" to resume
3. Answer 50 more questions
4. Close browser

**Wednesday (1 hour available):**
1. Resume Practice EPPP 1
2. Complete remaining 75 questions
3. View results with total time

### Scenario 2: Cross-Device Study
**At home (Desktop):**
1. Start AR Exam 1
2. Answer 80 questions
3. Export progress from Dashboard
4. Email to self

**During lunch (Phone):**
1. Open email, download `.eppp` file
2. Go to Dashboard, click Import
3. Resume AR Exam 1 from In-Progress section
4. Answer 40 more questions
5. Export again

**At home later (Desktop):**
1. Import updated `.eppp` file
2. Resume and complete final 55 questions
3. Check results

### Scenario 3: Interrupted Session
**Power outage during test:**
1. Wait for power to return
2. Open browser and go to same test
3. Click "OK" to resume
4. Continue from last saved answer
5. Time tracking continues where you left off

## Technical Details

### Storage Locations
- **Progress**: `localStorage` key pattern: `eppp_progress_{email}_{testname}`
- **Completed**: `localStorage` key: `eppp_user_{email}_tests`
- **User info**: `localStorage` key: `eppp_user`

### File Format
Export files (`.eppp`) are JSON format:
```json
{
  "version": "1.1",
  "exportDate": "2024-01-15T10:30:00.000Z",
  "user": { "name": "...", "email": "..." },
  "attempts": [...],
  "incompleteTests": [
    {
      "testName": "Practice EPPP 1",
      "answers": { "0": "B", "1": "C", ... },
      "startTime": 1705315800000,
      "elapsedTime": 1800000,
      "answeredCount": 45,
      "totalQuestions": 175,
      "savedAt": "2024-01-15T10:30:00.000Z"
    }
  ]
}
```

### Auto-Save Frequency
- Triggers: After **every answer selection**
- Delay: Immediate (no throttling)
- What's saved: All answers, question count, timestamps

## Support

### Questions?
If you have questions about the Resume feature:
1. Re-read the relevant section above
2. Check Troubleshooting section
3. Try clearing progress and restarting

### Feature Requests
Contact the administrator to suggest improvements:
- Longer auto-save intervals?
- Cloud sync instead of manual export?
- Additional progress statistics?

## Version History

### v1.1 (Current)
- ✅ Auto-save progress after each answer
- ✅ Resume prompt on test load
- ✅ Time tracking with display
- ✅ Export/import for incomplete tests
- ✅ Dashboard "In-Progress Tests" section
- ✅ Clear progress functionality

### Future Enhancements (Planned)
- ⏳ Cloud sync (no manual export needed)
- ⏳ Progress sync across devices automatically
- ⏳ Practice mode vs. Timed mode toggle
- ⏳ Bookmark questions for review

---

**Last Updated**: January 2024  
**Compatible With**: All EPPP Practice Tests (AR Exam 1-8, Practice EPPP 1-7)
