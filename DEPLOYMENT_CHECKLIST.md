# Deployment Checklist

## 📋 Pre-Deployment Checklist

### Security
- [ ] `.env` file is in `.gitignore`
- [ ] Firebase JSON file is in `.gitignore`
- [ ] No API keys hardcoded in source files
- [ ] `.env.example` has only placeholder values
- [ ] Sensitive files removed from git tracking

### Code Ready
- [ ] All features tested locally
- [ ] Web interface works: `python web_app.py`
- [ ] CLI commands work
- [ ] Database connections successful
- [ ] Weather API calls successful

### Files Created
- [ ] `Procfile` (for deployment)
- [ ] `runtime.txt` (Python version)
- [ ] `requirements.txt` (with gunicorn)
- [ ] `.gitignore` (updated)
- [ ] `DEPLOYMENT.md` (instructions)

---

## 🚀 Deployment Steps

### Phase 1: GitHub (Version Control)

1. **Initialize Git**
   ```bash
   git init
   ```
   - [ ] Done

2. **Remove Sensitive Files**
   ```bash
   git rm --cached .env
   ```
   - [ ] Done

3. **Add All Files**
   ```bash
   git add .
   ```
   - [ ] Done

4. **Commit**
   ```bash
   git commit -m "Sprint 1 MVP"
   ```
   - [ ] Done

5. **Create GitHub Repo**
   - Go to github.com
   - Create new repository: `climatovate-sprint1`
   - [ ] Done

6. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/climatovate-sprint1.git
   git branch -M main
   git push -u origin main
   ```
   - [ ] Done

7. **Verify**
   - Check GitHub repo
   - Confirm `.env` is NOT there
   - Confirm Firebase JSON is NOT there
   - [ ] Done

---

### Phase 2: Render Deployment (Hosting)

1. **Sign Up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - [ ] Done

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect GitHub repository
   - [ ] Done

3. **Configure Service**
   - Name: `climatovate-sprint1`
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn web_app:app`
   - Plan: Free
   - [ ] Done

4. **Prepare Firebase Config**
   
   **On Windows PowerShell:**
   ```powershell
   $content = Get-Content "C:\Users\3CHUB\Downloads\climatovate--mvp1-sprint-firebase-adminsdk-fbsvc-40d0c7999a.json" -Raw
   $bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
   $base64 = [Convert]::ToBase64String($bytes)
   $base64 | Out-File firebase_base64.txt
   ```
   - [ ] Done
   - [ ] Copy content from `firebase_base64.txt`

5. **Add Environment Variables in Render**
   
   In Render dashboard, add these:
   
   - [ ] `WEATHER_API_KEY` = `6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD`
   - [ ] `WEATHER_API_BASE_URL` = `https://api.tomorrow.io/v4`
   - [ ] `APP_ID` = `climatovate`
   - [ ] `USER_ID` = `admin`
   - [ ] `FIREBASE_CONFIG_BASE64` = (paste base64 content)
   - [ ] `SECRET_KEY` = (generate random string)

6. **Deploy**
   - Click "Create Web Service"
   - Wait for build (5-10 minutes)
   - [ ] Done

7. **Test Deployment**
   - Open your Render URL: `https://climatovate-sprint1.onrender.com`
   - Test dashboard loads
   - Test farmer enrollment
   - Test alert generation
   - [ ] Done

---

## ✅ Post-Deployment

### Verify Everything Works

- [ ] Dashboard loads without errors
- [ ] Can enroll a farmer
- [ ] Can generate alerts
- [ ] Can add feedback
- [ ] Weather forecast query works
- [ ] All metrics display correctly

### Share with Stakeholders

- [ ] Copy deployment URL
- [ ] Share with team
- [ ] Document any issues
- [ ] Collect feedback

### Monitor

- [ ] Check Render logs for errors
- [ ] Monitor free tier usage
- [ ] Track uptime
- [ ] Note any performance issues

---

## 🔧 Troubleshooting

### Build Fails
- [ ] Check requirements.txt
- [ ] Verify Python version in runtime.txt
- [ ] Review build logs in Render

### App Crashes
- [ ] Verify all environment variables set
- [ ] Check Firebase config base64 is correct
- [ ] Review application logs

### Database Errors
- [ ] Verify Firebase service account permissions
- [ ] Check Firestore is enabled
- [ ] Test Firebase config locally first

### API Errors
- [ ] Verify Weather API key is correct
- [ ] Check Tomorrow.io account status
- [ ] Test API calls locally first

---

## 📊 Success Criteria

Deployment is successful when:

- [x] Code pushed to GitHub
- [ ] App deployed to Render
- [ ] Dashboard accessible via public URL
- [ ] All features work in production
- [ ] No sensitive data exposed
- [ ] Environment variables configured
- [ ] Database connections working
- [ ] API calls successful

---

## 📞 Support Resources

- **Render Docs**: https://render.com/docs
- **GitHub Docs**: https://docs.github.com
- **Flask Deployment**: https://flask.palletsprojects.com/en/latest/deploying/
- **Firebase Admin SDK**: https://firebase.google.com/docs/admin/setup

---

## 🎉 Completion

When all checkboxes are marked:
- ✅ Your app is live!
- ✅ Accessible to anyone with the URL
- ✅ Ready for testing with real farmers
- ✅ Can collect feedback and iterate

**Your deployment URL**: `https://climatovate-sprint1.onrender.com`

Share this with your team and start testing! 🚀
