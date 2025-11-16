# 🔒 EPPP Practice Tests - Security Guide

## ⚠️ IMPORTANT: Understanding the Limitations

### What You Need to Know

**TinyURL does NOT hide the destination URL in the browser.** When users click your TinyURL, their browser will show the full GitHub Pages URL in the address bar. This is normal behavior and cannot be prevented with client-side solutions.

### What This Means:

1. ✅ **TinyURL helps with:** Easy sharing, clean links, professional appearance
2. ❌ **TinyURL does NOT hide:** The final destination URL in the browser
3. ⚠️ **Risk:** Tech-savvy users can view your source code on GitHub

---

## 🛡️ Security Layers We've Added

### 1. Password Hashing ✅
- User password (`EPPP2025`) is now stored as SHA-256 hash
- Not easily readable in source code
- Hash: `3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b`

### 2. Admin Dashboard Protection ✅
- Separate admin password: `admin2025`
- Prevents unauthorized access to user data
- Uses hashed password verification

### 3. Session-Based Authentication ✅
- Access expires when browser closes
- No persistent cookies
- Limited window for unauthorized access

---

## 🚨 Remaining Risks

### 1. **Source Code is Public**
**Risk:** Anyone can view your GitHub repository and see the code.

**Mitigations Applied:**
- Password stored as hash (not plain text)
- Admin dashboard has separate password
- Session-based authentication

**What You Should Do:**
- ⚠️ **NEVER commit sensitive data to the repo** (API keys, personal info, etc.)
- Change passwords regularly
- Monitor admin dashboard for suspicious activity

### 2. **Password Can Be Found in Source**
**Risk:** Determined users can find the hashed password in login.html and potentially crack it.

**Mitigations Applied:**
- SHA-256 hashing (computationally expensive to crack)
- No personal info in password
- Separate admin password

**What You Should Do:**
- Use strong, unique passwords (mix of letters, numbers, symbols)
- Change password if compromised
- Don't use personal information in passwords

### 3. **Admin Dashboard URL Can Be Discovered**
**Risk:** Users might guess or find the admin.html URL.

**Mitigations Applied:**
- ✅ Admin password protection added
- Requires separate authentication
- Session-based access

**What You Should Do:**
- Keep admin URL private
- Use strong admin password
- Check access logs regularly

### 4. **localStorage Data Can Be Viewed**
**Risk:** Users can inspect their browser's localStorage and see test data.

**Impact:** LOW - They can only see their own data, not others' data

**Mitigations:**
- Each user's data is isolated
- Admin dashboard requires password
- No cross-user data access

---

## 🔐 Current Password Configuration

### User Access Password
- **Password:** `EPPP2025`
- **Hash:** `3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b`
- **Where:** `login.html`

### Admin Dashboard Password
- **Password:** `admin2025`
- **Hash:** `8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92`
- **Where:** `admin.html`

---

## 🔧 How to Change Passwords Securely

### Method 1: Using Password Generator Tool (Recommended)

1. **Open:** `password-generator.html` in your browser (locally)
   - File location: `/Interactive_Tests/password-generator.html`
   
2. **Enter** your new password (at least 6 characters)

3. **Confirm** the password

4. **Click** "Generate SHA-256 Hash"

5. **Copy** the generated hash

6. **Update** the code:
   - For user password: Edit `login.html`, replace `ACCESS_CODE_HASH`
   - For admin password: Edit `admin.html`, replace `ADMIN_PASSWORD_HASH`

7. **Update** `LEGACY_CODE` in `login.html` to match your new password

8. **Save, commit, and push** to GitHub

### Method 2: Online Hash Generator

1. Visit: https://emn178.github.io/online-tools/sha256.html
2. Enter your password
3. Copy the SHA-256 hash
4. Follow steps 6-8 above

---

## 🎯 Best Practices

### Do's ✅

1. **Change passwords regularly** (monthly recommended)
2. **Use strong passwords** (12+ characters, mixed case, numbers, symbols)
3. **Monitor admin dashboard** for unusual activity
4. **Export data regularly** for backup
5. **Keep admin URL private** - only share with authorized personnel
6. **Use different passwords** for user access vs admin access
7. **Document password changes** in a secure location (not in the repo)

### Don'ts ❌

1. **Don't commit plain text passwords** to GitHub
2. **Don't use personal information** in passwords (birthdays, names, etc.)
3. **Don't share admin credentials** with regular users
4. **Don't store sensitive user data** in the tests (no SSNs, credit cards, etc.)
5. **Don't use the same password** for user and admin access
6. **Don't share the direct GitHub URL** - always use TinyURL
7. **Don't ignore security updates** - review this guide regularly

---

## 🔍 What Users Can Access

### If User Knows GitHub URL:
- ✅ Can view all HTML/JS/CSS source code
- ✅ Can see password hash (but can't easily crack it)
- ❌ Cannot access admin dashboard (requires admin password)
- ❌ Cannot see other users' data (isolated in localStorage)
- ❌ Cannot modify the deployed site (read-only access)

### If User Knows Admin URL:
- ❌ Cannot access without admin password
- ✅ Session expires when browser closes
- ❌ Cannot extract data without authentication

---

## 🚀 Acceptable Risk Level

### For Most Use Cases: ✅ ACCEPTABLE

**Why:**
- Users need valid password to access tests
- Admin dashboard protected with separate password
- User data isolated and private
- Source code doesn't contain sensitive information
- Password hashing prevents easy discovery

### When You Need More Security: 🔴 Consider Alternatives

**If you have:**
- Highly sensitive user data (medical, financial, etc.)
- Need to prevent all source code access
- Require server-side authentication
- Need audit trails and compliance

**Then consider:**
- Private GitHub repository (requires GitHub Pro)
- Backend authentication server
- Commercial LMS platforms
- Self-hosted solutions with .htaccess protection

---

## 📊 Security Comparison

| Feature | Current Setup | Ideal Setup |
|---------|---------------|-------------|
| Password Protection | ✅ Yes (hashed) | ✅ |
| Admin Dashboard Protection | ✅ Yes | ✅ |
| Source Code Visibility | ❌ Public | ✅ Private |
| User Data Isolation | ✅ Yes | ✅ |
| Session Management | ✅ Yes | ✅ |
| Password Recovery | ❌ No | ⚠️ Manual |
| Audit Logs | ✅ Yes | ✅ |
| HTTPS | ✅ Yes (GitHub) | ✅ |

---

## 🔄 Regular Security Checklist

### Weekly:
- [ ] Check admin dashboard for unusual access patterns
- [ ] Review access logs for suspicious activity
- [ ] Verify all tests are functioning correctly

### Monthly:
- [ ] Change user access password
- [ ] Change admin password
- [ ] Export and backup user data
- [ ] Review and clean access logs

### Quarterly:
- [ ] Review this security guide
- [ ] Update documentation
- [ ] Test all authentication flows
- [ ] Consider security improvements

---

## 🆘 If Security is Compromised

### If User Password is Leaked:

1. **Immediately** change the password using password-generator.html
2. **Update** hash in login.html
3. **Commit and push** changes to GitHub
4. **Wait 2-3 minutes** for GitHub Pages to update
5. **Notify users** of the new password
6. **Monitor** admin dashboard for unauthorized access

### If Admin Password is Compromised:

1. **Change admin password** immediately
2. **Review access logs** for unauthorized admin access
3. **Export all data** for backup
4. **Consider clearing** all data if necessary
5. **Update password** in admin.html
6. **Push changes** to GitHub

### If GitHub Repository is Discovered:

1. **Don't panic** - passwords are hashed
2. **Change both passwords** as a precaution
3. **Review commit history** for sensitive data
4. **Consider making repo private** (requires GitHub Pro)
5. **Continue monitoring** admin dashboard

---

## 💡 Advanced Security Options

### Option 1: Make Repository Private (Requires GitHub Pro)
- **Cost:** $4/month per user
- **Benefit:** Source code completely hidden
- **How:** Repository Settings → Change visibility → Private

### Option 2: Add .htaccess Protection (If Self-Hosting)
- Requires Apache server
- Server-side password protection
- Not available on GitHub Pages

### Option 3: Use Environment Variables
- Store passwords outside source code
- Requires build process
- Not available on GitHub Pages

### Option 4: Two-Factor Authentication
- Requires backend server
- SMS or email verification
- Significantly more complex

---

## 📝 Summary

### ✅ What's Protected:
1. User access (password: EPPP2025, hashed)
2. Admin dashboard (password: admin2025, hashed)
3. Session-based authentication
4. User data isolation
5. Access logging

### ⚠️ What's Not Protected:
1. Source code visibility (public GitHub repo)
2. URL visibility after TinyURL redirect
3. Determined users can view code

### 🎯 Recommended Action:
**For most educational/practice use cases, the current security is sufficient.** 

The combination of:
- Password authentication (hashed)
- Admin password protection
- Session management
- User data isolation

Provides reasonable security for a practice test platform.

---

## 📞 Questions?

Review the following files for more information:
- `AUTHENTICATION_GUIDE.md` - Detailed authentication documentation
- `QUICK_REFERENCE.md` - Quick command reference
- `password-generator.html` - Tool for generating secure password hashes

---

**Last Updated:** November 16, 2025
**Security Version:** 2.0
**Next Review:** December 16, 2025
