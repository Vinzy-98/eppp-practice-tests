# Deployment Guide: EPPP Interactive Tests to GitHub Pages

This guide will help you deploy your EPPP interactive tests to GitHub Pages, making them accessible to anyone with the URL.

## ✅ Prerequisites Complete

- ✓ Git repository initialized
- ✓ All files committed to main branch
- ✓ 15 untimed interactive tests
- ✓ 15 EPPP format timed tests
- ✓ Index pages for both formats
- ✓ README.md file

## 🚀 Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Repository settings:
   - **Name:** `eppp-practice-tests` (or your preferred name)
   - **Description:** "EPPP Interactive Practice Tests with Timer and Navigation"
   - **Visibility:** 
     - Choose **Public** to make tests accessible to anyone
     - Choose **Private** if you want to control access (GitHub Pages works for private repos too)
   - **DO NOT** initialize with README (we already have one)
4. Click "Create repository"

### Step 2: Link Local Repository to GitHub

GitHub will show you instructions. In your terminal, run:

```bash
cd /Users/vagrawal/Documents/Personal/Dhriti\ -\ EPPP/Interactive_Tests

# Add GitHub repository as remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/vagrawal/eppp-practice-tests.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Scroll down and click **Pages** (left sidebar)
4. Under "Source":
   - Select branch: **main**
   - Select folder: **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes for deployment

### Step 4: Access Your Tests

GitHub will show you the URL (typically):
```
https://YOUR_USERNAME.github.io/REPO_NAME/
```

**Example:**
```
https://vagrawal.github.io/eppp-practice-tests/
```

This is your **main page** with links to both test formats!

### Direct Links to Test Formats:

- **Untimed Practice Tests:** `https://YOUR_USERNAME.github.io/REPO_NAME/`
- **EPPP Format (Timed):** `https://YOUR_USERNAME.github.io/REPO_NAME/EPPP_Format/index_eppp.html`

## 🔄 Updating Tests Later

If you need to update any tests in the future:

```bash
cd /Users/vagrawal/Documents/Personal/Dhriti\ -\ EPPP/Interactive_Tests

# Make your changes, then:
git add -A
git commit -m "Description of changes"
git push origin main
```

GitHub Pages will automatically redeploy (takes 1-2 minutes).

## 🌐 Sharing with Users

Once deployed, share the URL with anyone who needs access. They can:

### Untimed Practice Mode:
- Take tests at their own pace
- Review answers anytime
- No time pressure
- Perfect for learning and studying

### EPPP Format Mode:
- Realistic exam simulation
- Countdown timer (1.13 min per question)
- Question navigator
- Mark questions for review
- Time warnings (5 min, 1 min)
- Auto-submit when time expires
- Download detailed results

## 💾 How User Data Works

**Important:** All test data is stored **locally in each user's browser**:
- ✅ Each user gets their own independent experience
- ✅ Scores and answers are private to each user
- ✅ No server required - everything runs in the browser
- ✅ Users can download their results as text files
- ⚠️ If users clear browser cache, their progress will be lost
- ⚠️ Different devices/browsers = separate progress

This means:
- **No database needed** - tests are fully client-side
- **No user accounts** - instant access for everyone
- **Privacy-friendly** - no tracking or data collection
- **Works offline** - after initial load, tests work without internet

## 🔒 Access Control Options

### Public Access (Current Setup)
- Anyone with the URL can access tests
- Best for open educational resources

### Private Repository with Access Control
1. Make repository private in GitHub settings
2. Add specific GitHub users as collaborators
3. Only collaborators can access the GitHub Pages site
4. Go to Settings → Manage access → Invite collaborators

### Password Protection (Advanced)
If you need password protection:
1. GitHub Pages doesn't support built-in passwords
2. Options:
   - Use a separate hosting service with authentication (Netlify, Vercel)
   - Add simple JavaScript password prompt (can be bypassed, not secure)
   - Use GitHub private repo + collaborators (most secure)

## 📱 Browser Compatibility

Tests work on all modern browsers:
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🆘 Troubleshooting

### Issue: "git push" asks for username/password
**Solution:** Use Personal Access Token instead of password
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scope: `repo`
4. Copy token and use as password when pushing

### Issue: GitHub Pages showing 404
**Solution:** 
- Wait 2-3 minutes after enabling Pages
- Check branch and folder settings in Pages configuration
- Ensure `index.html` exists in root directory

### Issue: Tests work locally but not on GitHub Pages
**Solution:**
- All files are already using relative paths (should work)
- Check browser console for errors (F12)
- Ensure all HTML files are committed to repository

## 📊 Current Statistics

- **Total Tests:** 30 (15 untimed + 15 EPPP format)
- **Total Questions:** 3,043
- **Test Modes:** 2 (Practice & EPPP Format)
- **Repository Size:** ~8-10 MB
- **Load Time:** 1-3 seconds per test (depends on internet speed)

## 🎓 Recommended Workflow for Students

1. **Start with Untimed Practice Tests**
   - Learn at your own pace
   - Focus on understanding concepts
   - Review correct answers immediately

2. **Progress to EPPP Format Tests**
   - Simulate real exam conditions
   - Practice time management
   - Get comfortable with test interface

3. **Track Progress**
   - Download results after each test
   - Keep results files for comparison
   - Identify weak areas for focused study

---

## Quick Command Reference

```bash
# Navigate to repository
cd /Users/vagrawal/Documents/Personal/Dhriti\ -\ EPPP/Interactive_Tests

# Check status
git status

# Add and commit changes
git add -A
git commit -m "Your message"

# Push to GitHub
git push origin main

# View remote URL
git remote -v
```

---

**Need help?** Check the README.md file or GitHub Pages documentation at https://pages.github.com
