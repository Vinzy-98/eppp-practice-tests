# 📊 User Dashboard Guide

## What's New!

Your EPPP tests now have a **personal dashboard** where you can track your progress, see analytics, and manage test attempts!

---

## 🎯 Key Features

### 1. **Automatic User Identification**
When you first open any test, you'll be prompted to enter:
- Your name (required)
- Email (optional - for your records)

This information is stored **only on your device** and is never shared with anyone.

### 2. **Personal Dashboard**
Access your dashboard by clicking **"📊 My Dashboard"** from:
- Any test page (top right)
- Main index page
- EPPP Format index page

### 3. **Progress Tracking**
Your dashboard shows:
- **Total Attempts** - How many tests you've taken
- **Unique Tests** - Different tests you've tried
- **Average Score** - Your overall performance
- **Total Correct** - Cumulative correct answers
- **Recent Improvement** - Trend of last 5 vs first 5 attempts

### 4. **Visual Analytics**

#### Progress Over Time Chart
- Line graph showing score trends
- See improvement across all attempts
- Hover for details on each attempt

#### Performance by Test Chart
- Bar graph comparing average scores per test
- Identify your strongest and weakest areas
- Focus study efforts where needed

### 5. **Test History**
View all your attempts with:
- Test name and attempt number
- Date and time taken
- Detailed scores (correct/incorrect/unanswered)
- Improvement badges (↑ better, ↓ needs work)
- **Retake button** to try again

### 6. **Filter by Test**
- Click "All Tests" to see everything
- Click specific test names to filter
- Quickly find attempts for any test

### 7. **Retake Functionality**
From your dashboard:
1. Find any test in your history
2. Click **"Retake Test"**
3. Start a new attempt immediately
4. Previous attempts are preserved for comparison

### 8. **Export Your Data**
Click **"📥 Export Data"** to download:
- All your attempts
- User information
- Scores and timestamps
- JSON format for analysis in Excel/other tools

---

## 🚀 How to Use

### First Time
1. Open any test
2. Enter your name (and optional email)
3. Click "Start Test"
4. Take the test normally
5. After completion, your attempt is automatically saved

### Subsequent Tests
1. Your name is remembered
2. Each new test automatically tracks as a new attempt
3. View progress in dashboard anytime

### Retaking a Test
1. Open dashboard
2. Find the test in your history
3. Click "Retake Test"
4. Your new attempt will be numbered (Attempt #2, #3, etc.)
5. Compare scores to see improvement

### Viewing Analytics
1. Dashboard shows real-time stats
2. Charts update automatically with each test
3. Filter by test to see specific progress
4. Look for improvement badges in history

---

## 💡 Pro Tips

### Track Your Progress
- Take tests regularly to see trends
- Compare attempt #1 vs #2 vs #3 for each test
- Focus on tests with lower average scores
- Celebrate improvements! 🎉

### Use the Charts
- **Progress Over Time** shows overall learning curve
- **Performance by Test** reveals strengths/weaknesses
- Downward trends? Review that content area
- Upward trends? You're mastering it!

### Export for Analysis
- Download your data monthly
- Keep records of long-term progress
- Share with instructors if needed
- Backup before clearing browser data

### Multiple Attempts Strategy
1. **First attempt** - Baseline (no prep)
2. **Second attempt** - After reviewing incorrect answers
3. **Third attempt** - After focused study
4. Track improvement to validate study methods

---

## 🔒 Privacy & Data

### Where is My Data Stored?
- **Locally in your browser** (localStorage)
- **Never uploaded to servers**
- **Not shared with anyone**
- **Private to your device**

### Accessing from Multiple Devices?
- Each device has separate data
- Use "Export Data" to backup
- Import not currently supported (coming soon)

### Clearing Data
If you clear browser cache/localStorage:
- Your history will be erased
- Export data first to backup!
- You can re-enter your name to start fresh

### Changing Users
Click **"👤 Change User"** to:
- Switch to different user profile
- Take tests as someone else
- Previous user data is preserved (not deleted)

---

## 📊 Dashboard Overview

```
┌─────────────────────────────────────────────────┐
│  👤 User Avatar  Welcome back, [Name]!         │
│                  [email]                        │
│                                                 │
│  [Export Data]  [Change User]  [Take Tests]    │
├─────────────────────────────────────────────────┤
│  [15]          [5]           [85%]          📈  │
│  Attempts    Unique Tests  Avg Score   +5% ↑   │
├─────────────────────────────────────────────────┤
│  📈 Progress Over Time                          │
│  [Line Chart showing score trends]              │
├─────────────────────────────────────────────────┤
│  📊 Performance by Test                         │
│  [Bar Chart comparing test scores]              │
├─────────────────────────────────────────────────┤
│  📚 Test History                                │
│  [All Tests] [AR Exam 1] [Practice EPPP 1]...  │
│                                                 │
│  ┌───────────────────────────────────────┐     │
│  │ AR Exam 1            ↑ +8%            │     │
│  │ Attempt #2 • Nov 16, 2025             │     │
│  │ ✓ 180 • ✗ 25 • ⚠ 6           [92%]   │     │
│  │                         [Retake Test] │     │
│  └───────────────────────────────────────┘     │
└─────────────────────────────────────────────────┘
```

---

## 🎓 Example Workflows

### Workflow 1: Study & Improve
1. Take AR Exam 1 (baseline)
2. Check dashboard - see score
3. Review incorrect answers
4. Study weak areas
5. Retake AR Exam 1 from dashboard
6. Compare improvement badge
7. Repeat until mastery

### Workflow 2: Comprehensive Assessment
1. Take all 15 tests over time
2. Review dashboard analytics
3. Identify lowest-scoring tests
4. Focus study on those areas
5. Retake weak tests
6. Track overall average improvement

### Workflow 3: Exam Preparation
1. Start with untimed practice tests
2. Build confidence and knowledge
3. Progress to EPPP format (timed)
4. Track time management skills
5. Compare timed vs untimed performance
6. Adjust strategy based on dashboard insights

---

## ❓ FAQ

**Q: Can I delete individual attempts?**  
A: Not currently - use browser localStorage inspector or clear all data and start fresh.

**Q: Can I share my dashboard with others?**  
A: Export your data and share the JSON file. Recipients can view it in any JSON viewer.

**Q: Does the dashboard work offline?**  
A: Yes! After initial page load, everything works offline (stored locally).

**Q: How many attempts can I track?**  
A: Unlimited! However, browser storage limits apply (typically 5-10MB).

**Q: Can I see other users' dashboards?**  
A: No - each user's data is isolated to their own browser.

**Q: What if I accidentally close the browser?**  
A: Your data is saved! Just reopen and continue where you left off.

---

## 🆘 Troubleshooting

**Dashboard shows "No test attempts yet"**
- Take a test first
- Ensure you completed a test (clicked "Check Answers")
- Check that you entered your name when prompted

**Charts not displaying**
- Ensure internet connection (Chart.js loads from CDN)
- Try refreshing the page
- Check browser console for errors (F12)

**User name not saved**
- Check browser doesn't block localStorage
- Try different browser
- Don't use private/incognito mode

**Can't click "Retake Test"**
- Make sure the test file still exists
- Check file names haven't changed
- Open test manually if needed

---

## 🚀 Coming Soon

Future enhancements planned:
- Import/export for cross-device sync
- Detailed question-level analytics
- Strength/weakness by topic
- Study recommendations
- Comparison with average scores
- Goal setting and milestones

---

## 💬 Feedback

Have suggestions for the dashboard? Export your feature requests along with your data!

---

**Happy Studying! 📚✨**
