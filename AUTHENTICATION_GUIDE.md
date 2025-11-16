# EPPP Practice Tests - Authentication & Admin Guide

## 🔐 Authentication System

### Password Access

The EPPP Practice Tests now require a password for access. This ensures privacy and controlled access to your test materials.

**Default Access Code:** `EPPP2024`

### How to Change the Password

1. **Open** `login.html` in a text editor
2. **Find** line 137 (approximately):
   ```javascript
   const ACCESS_CODE = 'EPPP2024'; // Change this to your desired password
   ```
3. **Change** `'EPPP2024'` to your new password
4. **Save** the file
5. **Commit and push** to GitHub (if using GitHub Pages)

**Example:**
```javascript
const ACCESS_CODE = 'MySecurePassword123';
```

### Password Best Practices

- Use a mix of letters, numbers, and symbols
- Make it memorable but not easily guessable
- Don't share it publicly
- Change it periodically for security
- Keep a backup copy in a secure location

---

## 📊 Admin Dashboard

### Accessing the Admin Dashboard

The admin dashboard allows you to monitor user activity, access logs, and test performance.

**URL:** `https://your-site-url.github.io/eppp-practice-tests/admin.html`

Or locally: `file:///path/to/Interactive_Tests/admin.html`

### Dashboard Features

#### 1. **Key Statistics**
- **Unique Users**: Count of distinct users/sessions
- **Total Accesses**: Number of times the site has been accessed
- **Tests Taken**: Total number of tests completed
- **Average Score**: Overall average test performance

#### 2. **Access Over Time Chart**
- Visual representation of daily access patterns
- Shows the last 7 days of activity
- Helps identify peak usage times

#### 3. **Test Performance Chart**
- Average scores for each test
- Compare difficulty across different exams
- Identify which tests need more practice

#### 4. **Access Logs Table**
- Detailed log of every login attempt
- Shows date, time, and session ID
- Last 50 entries displayed

#### 5. **User Activity Summary**
- Individual user statistics
- Tests taken per user
- Average score per user
- Last activity date

### Dashboard Actions

#### Refresh Data
Click the **🔄 Refresh** button to reload all statistics from localStorage.

#### Export Data
- **📄 Export as JSON**: Downloads complete data backup including all users, tests, and logs
- **📊 Export as CSV**: Downloads user activity in spreadsheet format

#### Clear All Data
⚠️ **Warning**: This permanently deletes ALL user data, access logs, and test results.

Use this to:
- Reset for a new cohort of users
- Clean up test data
- Start fresh

**This action cannot be undone!**

---

## 🔒 How Authentication Works

### Session-Based Authentication

1. **User visits site** → Redirected to `login.html`
2. **Enters password** → Verified against `ACCESS_CODE`
3. **Correct password** → Session created, redirected to home
4. **Session stored** → Uses `sessionStorage` (lasts until browser closes)

### Security Features

- **Session Storage**: Authentication expires when browser closes
- **Auto-redirect**: All protected pages check for authentication
- **Access Logging**: Every successful login is tracked
- **No server required**: All authentication is client-side

### Protected Pages

All these pages require authentication:
- `index.html` (landing page)
- `tests.html` (test browser)
- `dashboard.html` (user dashboard)
- All 15 interactive test files (`AR_Exam_*.html`, `Practice_EPPP_*.html`)
- All 15 EPPP format tests (`EPPP_Format/*_EPPP.html`)

**Total: 32 protected pages**

---

## 📈 User Tracking

### What Gets Tracked?

1. **Access Logs**
   - Timestamp of each login
   - Date and time
   - Session ID (browser fingerprint)

2. **User Information**
   - Name (from user input)
   - Email (from user input)
   - Test history
   - Scores and completion dates

3. **Test Activity**
   - Which tests were taken
   - Scores achieved
   - Time spent on tests
   - Number of attempts

### Privacy & Data Storage

- **All data stored locally** in browser's localStorage
- **No server transmission** - completely client-side
- **User controls their data** - can clear anytime from user dashboard
- **Admin access** - only accessible via admin.html
- **Session-based** - authentication expires when browser closes

### Session ID Generation

Session IDs are generated from:
- User agent string
- Browser language
- Current date
- Screen resolution

This creates a reasonably unique identifier without being invasive.

---

## 🛠️ Troubleshooting

### Users Can't Access Tests

**Problem**: Users stuck at login page

**Solutions**:
1. Verify they're using the correct password
2. Check that JavaScript is enabled in their browser
3. Try clearing browser cache and cookies
4. Test in private/incognito mode
5. Try a different browser

### Admin Dashboard Shows No Data

**Problem**: Dashboard is empty

**Solutions**:
1. Ensure at least one user has logged in
2. Check that localStorage is enabled
3. Try clicking the Refresh button
4. Check browser console for errors (F12)
5. Verify users completed at least one test

### Password Not Working

**Problem**: Access code doesn't work after changing

**Solutions**:
1. Check for typos in `login.html`
2. Ensure you saved the file after editing
3. Clear browser cache
4. If using GitHub Pages, wait 2-3 minutes for deployment
5. Verify the JavaScript syntax is correct (no missing quotes)

### Data Disappeared

**Problem**: User data or access logs are gone

**Solutions**:
1. Check if localStorage was cleared by user
2. Verify browser allows localStorage
3. Check if browser's private mode was used (doesn't persist)
4. Look for exported backup files (JSON/CSV)
5. Check if "Clear All Data" was accidentally clicked in admin

---

## 🔧 Advanced Configuration

### Customizing Login Page

Edit `login.html`:

**Change colors:**
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

**Change title:**
```html
<h1>🔒 EPPP Practice Tests</h1>
```

**Change info text:**
```html
<div class="info-box">
    <strong>🔐 Privacy First:</strong> Your custom message here.
</div>
```

### Customizing Admin Dashboard

Edit `admin.html`:

**Change chart colors:**
```javascript
backgroundColor: 'rgba(102, 126, 234, 0.2)',
borderColor: 'rgba(102, 126, 234, 1)',
```

**Adjust table display:**
```javascript
const recentLogs = accessLogs.slice(-50).reverse(); // Show last 50 logs
```

### Multiple Passwords (Admin + User)

To add admin authentication to `admin.html`:

```javascript
// Add at the top of admin.html <script> section
const ADMIN_PASSWORD = 'admin123';
const enteredPassword = prompt('Enter admin password:');
if (enteredPassword !== ADMIN_PASSWORD) {
    alert('Access denied!');
    window.location.href = 'index.html';
}
```

---

## 📋 Maintenance Checklist

### Weekly
- [ ] Review access logs in admin dashboard
- [ ] Check average test scores
- [ ] Monitor unique user count
- [ ] Export data backup (JSON)

### Monthly
- [ ] Change access password
- [ ] Export and archive user data (CSV)
- [ ] Review and analyze test performance trends
- [ ] Update test content if needed

### Quarterly
- [ ] Clear old access logs (keep last 3 months)
- [ ] Review and update documentation
- [ ] Check for browser compatibility issues
- [ ] Backup all data before major changes

---

## 📞 Support

### Common Questions

**Q: Can users create their own passwords?**
A: No, this is a single shared password system. All users use the same access code.

**Q: Can I see which specific user took which test?**
A: Yes, the User Activity Summary in admin dashboard shows per-user test history.

**Q: Is the data secure?**
A: Data is stored in browser localStorage, which is isolated per domain. However, anyone with admin access can view all data.

**Q: Can I have multiple admin accounts?**
A: The current system has no admin accounts. Anyone who knows the URL can access admin.html. Consider adding password protection (see Advanced Configuration).

**Q: What happens if I lose the password?**
A: Edit `login.html` to see or change the password. It's stored in plain text in the JavaScript code.

---

## 🚀 Quick Start Guide

### For Users
1. Visit the site URL
2. Enter the access code
3. Click "Access Tests"
4. Browse and take tests
5. View your progress in "My Dashboard"

### For Admins
1. Share the access code with authorized users
2. Monitor activity via `admin.html`
3. Export data regularly for backup
4. Change password periodically
5. Review test performance and adjust content as needed

---

## 📝 Files Reference

| File | Purpose | Protected |
|------|---------|-----------|
| `login.html` | Password authentication gate | No (entry point) |
| `index.html` | Professional landing page | Yes |
| `tests.html` | Test browser/selector | Yes |
| `dashboard.html` | User personal dashboard | Yes |
| `admin.html` | Admin analytics dashboard | No (should add protection) |
| `AR_Exam_*.html` | Interactive test files (8) | Yes |
| `Practice_EPPP_*.html` | Interactive test files (7) | Yes |
| `EPPP_Format/*_EPPP.html` | Timed test files (15) | Yes |

---

## 🎓 Best Practices

1. **Password Management**
   - Use a strong, unique password
   - Don't commit passwords to public repositories
   - Change password if shared with unauthorized users
   - Consider environment variables for passwords

2. **Data Privacy**
   - Inform users about data collection
   - Regularly export and backup data
   - Don't share user data without consent
   - Consider GDPR/privacy regulations if applicable

3. **Access Control**
   - Only share access code with authorized users
   - Add admin password protection
   - Monitor access logs regularly
   - Revoke access by changing password

4. **Maintenance**
   - Keep regular backups
   - Monitor dashboard weekly
   - Update test content as needed
   - Test authentication after any changes

---

**Last Updated:** November 16, 2025
**Version:** 2.0
