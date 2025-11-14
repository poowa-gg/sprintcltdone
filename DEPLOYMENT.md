# Deployment Guide

## 🚨 Important: Your App Needs a Python Server

Your Climatovate app is a **Flask backend application** that requires Python to run. Netlify only hosts static HTML/CSS/JS sites, so we need a different approach.

## ✅ Recommended: Deploy to Render (Free Tier)

Render offers free Python hosting perfect for your MVP.

### Step 1: Prepare for GitHub

1. **Update .gitignore** (already done)
2. **Remove sensitive files from tracking**:
   ```bash
   git rm --cached .env
   git rm --cached serviceAccountKey.json
   ```

### Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Sprint 1 MVP - Farmer Weather Alert System"

# Create GitHub repo (go to github.com and create new repo)
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/climatovate-sprint1.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Render

1. **Go to [render.com](https://render.com)** and sign up (free)

2. **Click "New +" → "Web Service"**

3. **Connect your GitHub repository**

4. **Configure the service:**
   - **Name**: climatovate-sprint1
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn web_app:app`
   - **Plan**: Free

5. **Add Environment Variables** (in Render dashboard):
   - `WEATHER_API_KEY`: Your Tomorrow.io API key
   - `WEATHER_API_BASE_URL`: https://api.tomorrow.io/v4
   - `APP_ID`: climatovate
   - `USER_ID`: admin
   - `FIREBASE_CONFIG`: (See Firebase setup below)

6. **Click "Create Web Service"**

### Step 4: Firebase Service Account for Render

Since you can't upload the JSON file directly, convert it to base64:

**On Windows:**
```powershell
# Convert Firebase JSON to base64
$content = Get-Content "C:\Users\3CHUB\Downloads\climatovate--mvp1-sprint-firebase-adminsdk-fbsvc-40d0c7999a.json" -Raw
$bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
$base64 = [Convert]::ToBase64String($bytes)
$base64 | Out-File firebase_base64.txt
```

Then in Render, add environment variable:
- `FIREBASE_CONFIG_BASE64`: (paste the base64 content)

**Update config.py to handle base64:**
```python
import os
import base64
import json
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_BASE_URL = os.getenv('WEATHER_API_BASE_URL', 'https://api.tomorrow.io/v4')
APP_ID = os.getenv('APP_ID', 'climatovate')
USER_ID = os.getenv('USER_ID', 'admin')

# Handle Firebase config (file path or base64)
FIREBASE_CONFIG = os.getenv('FIREBASE_CONFIG')
FIREBASE_CONFIG_BASE64 = os.getenv('FIREBASE_CONFIG_BASE64')

if FIREBASE_CONFIG_BASE64:
    # Decode base64 and save temporarily
    import tempfile
    config_json = base64.b64decode(FIREBASE_CONFIG_BASE64).decode('utf-8')
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
    temp_file.write(config_json)
    temp_file.close()
    FIREBASE_CONFIG = temp_file.name

# Alert thresholds
HEAVY_RAIN_THRESHOLD = 30  # mm in 3 hours
HEAT_STRESS_THRESHOLD = 40

# Validation
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable is required")
if not FIREBASE_CONFIG:
    raise ValueError("FIREBASE_CONFIG environment variable is required")
```

### Step 5: Access Your Deployed App

After deployment completes (5-10 minutes):
- Your app will be live at: `https://climatovate-sprint1.onrender.com`
- Free tier may sleep after inactivity (wakes up on first request)

---

## Alternative: Deploy to Railway

Railway is another great option with similar setup:

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables (same as Render)
6. Deploy!

---

## Alternative: Deploy to Heroku

Heroku also works but requires credit card (even for free tier):

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create climatovate-sprint1`
4. Set environment variables:
   ```bash
   heroku config:set WEATHER_API_KEY=your_key
   heroku config:set FIREBASE_CONFIG_BASE64=your_base64
   ```
5. Deploy: `git push heroku main`

---

## ❌ Why Not Netlify?

Netlify is for **static sites** (HTML/CSS/JS only). Your app needs:
- Python runtime
- Flask server
- Database connections
- API calls

These require a backend server, which Netlify doesn't provide.

**However**, you could:
1. Deploy backend to Render/Railway
2. Create a static frontend on Netlify that calls your backend API
3. This is a Sprint 2+ enhancement

---

## 🔒 Security Checklist Before Deploying

- [x] `.env` file in `.gitignore`
- [x] Firebase JSON in `.gitignore`
- [ ] Change Flask secret key in `web_app.py`
- [ ] Add authentication (Sprint 2)
- [ ] Use HTTPS only
- [ ] Set CORS policies
- [ ] Rate limiting on API endpoints

---

## 📝 GitHub Push Commands

```bash
# First time setup
git init
git add .
git commit -m "Initial commit - Sprint 1 MVP"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/climatovate-sprint1.git
git branch -M main
git push -u origin main

# Future updates
git add .
git commit -m "Update: description of changes"
git push
```

---

## 🎯 Recommended Deployment Flow

1. **Push to GitHub** (version control)
2. **Deploy to Render** (free Python hosting)
3. **Share URL** with stakeholders
4. **Iterate** based on feedback

Your app will be live and accessible to anyone with the URL!

---

## 🆘 Troubleshooting

**Build fails on Render:**
- Check requirements.txt has all dependencies
- Verify Python version in runtime.txt
- Check build logs for specific errors

**App crashes on startup:**
- Verify all environment variables are set
- Check Firebase config is properly decoded
- Review application logs in Render dashboard

**Database connection fails:**
- Verify Firebase service account has Firestore permissions
- Check FIREBASE_CONFIG_BASE64 is correctly encoded
- Ensure Firestore is enabled in Firebase console

**Weather API errors:**
- Verify WEATHER_API_KEY is correct
- Check Tomorrow.io account is active
- Ensure API key has proper permissions

---

## 📞 Need Help?

1. Check Render/Railway documentation
2. Review deployment logs
3. Test locally first: `python web_app.py`
4. Verify environment variables are set correctly
