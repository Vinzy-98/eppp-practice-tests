# 🔐 EPPP Authentication - Quick Reference

## For You (Admin)

### Access the Admin Dashboard
**URL:** https://vinzy-98.github.io/eppp-practice-tests/admin.html

View:
- Total unique users who accessed the site
- Total number of logins
- Tests taken and average scores
- Access logs with timestamps
- Individual user activity and performance
- Export data as JSON or CSV

### Current Password
**Access Code:** `EPPP2024`

### Change Password
1. Go to `login.html`
2. Find line 137: `const ACCESS_CODE = 'EPPP2024';`
3. Change to your new password
4. Save, commit, and push to GitHub

---

## For Users

### How to Access Tests
1. Visit: https://vinzy-98.github.io/eppp-practice-tests/
2. Enter access code: `EPPP2024`
3. Click "Access Tests"

### What Users See
- **Login page** (first time or new session)
- **Landing page** with overview
- **Test browser** with 30 tests available
- **Personal dashboard** with their own progress

---

## What's Protected

✅ **32 pages** now require password:
- Landing page (index.html)
- Test browser (tests.html)
- User dashboard (dashboard.html)
- 15 interactive tests (AR_Exam + Practice_EPPP)
- 15 EPPP format timed tests

❌ **Not protected** (intentional):
- Login page (entry point)
- Admin dashboard (you may want to add protection - see guide)

---

## Security Features

🔒 **Session-Based**
- Authentication expires when browser closes
- Uses `sessionStorage` (temporary)
- No persistent cookies

📊 **Access Tracking**
- Every login is logged with timestamp
- Session IDs track unique users
- All data stored locally (no server)

🔐 **Privacy First**
- No external data transmission
- All data in browser localStorage
- Users control their own data

---

## Key URLs

| Purpose | URL |
|---------|-----|
| Login (share with users) | https://vinzy-98.github.io/eppp-practice-tests/ |
| Admin Dashboard | https://vinzy-98.github.io/eppp-practice-tests/admin.html |
| URL Shortening Guide | See `URL_SHORTENING_GUIDE.md` |

---

## Quick Actions

### Share Access with Users
```
Hi! Here's your access to the EPPP Practice Tests:

URL: https://vinzy-98.github.io/eppp-practice-tests/
Access Code: EPPP2024

Enter the code when prompted. Your progress is saved automatically!
```

### View Statistics
1. Open admin dashboard
2. See real-time stats:
   - How many unique users
   - Total accesses
   - Tests taken
   - Average scores

### Export Data
1. Open admin dashboard
2. Scroll to bottom
3. Click "Export as JSON" or "Export as CSV"
4. Data downloads automatically

### Clear All Data
1. Open admin dashboard
2. Click "Clear All Data" button
3. Confirm twice (cannot be undone!)

---

## Next Steps

1. ✅ Test the login flow yourself
2. ✅ Visit admin dashboard to verify tracking works
3. ✅ Share the access code with your users
4. 📊 Monitor usage via admin dashboard
5. 🔄 Change password periodically
6. 💾 Export data regularly for backup

---

## Support

Full documentation in `AUTHENTICATION_GUIDE.md`:
- How to change password
- Troubleshooting guide
- Advanced configuration
- Security best practices
- Maintenance checklist

---

**Site deployed!** Wait 2-3 minutes for GitHub Pages to update, then test the new authentication system.
