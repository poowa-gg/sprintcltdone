================================================================================
CLIMATOVATE SPRINT 1 - DEPLOYMENT READY
================================================================================

YOUR APP IS READY TO DEPLOY!

IMPORTANT: Netlify won't work for your app because it's a Python Flask backend.
Use Render instead (free tier available).

================================================================================
QUICK START - 3 STEPS
================================================================================

STEP 1: PUSH TO GITHUB
-----------------------
git init
git add .
git commit -m "Sprint 1 MVP"
git remote add origin https://github.com/YOUR_USERNAME/climatovate-sprint1.git
git push -u origin main

STEP 2: CONVERT FIREBASE CONFIG
--------------------------------
Run in PowerShell:
$content = Get-Content "C:\Users\3CHUB\Downloads\climatovate--mvp1-sprint-firebase-adminsdk-fbsvc-40d0c7999a.json" -Raw
$bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
$base64 = [Convert]::ToBase64String($bytes)
$base64 | Out-File firebase_base64.txt

Copy the content from firebase_base64.txt

STEP 3: DEPLOY TO RENDER
-------------------------
1. Go to render.com and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Configure:
   - Build: pip install -r requirements.txt
   - Start: gunicorn web_app:app
5. Add environment variables:
   - WEATHER_API_KEY = 6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD
   - WEATHER_API_BASE_URL = https://api.tomorrow.io/v4
   - APP_ID = climatovate
   - USER_ID = admin
   - FIREBASE_CONFIG_BASE64 = [paste base64 from step 2]
   - SECRET_KEY = climatovate-production-2024
6. Click "Create Web Service"
7. Wait 10 minutes
8. Your app is live!

================================================================================
DETAILED GUIDES
================================================================================

DEPLOY_NOW.md              - Quick 3-step guide (START HERE)
GITHUB_SETUP.md            - Detailed GitHub instructions
DEPLOYMENT.md              - Full deployment guide
DEPLOYMENT_CHECKLIST.md    - Step-by-step checklist

================================================================================
WHY NOT NETLIFY?
================================================================================

Netlify = Static sites only (HTML/CSS/JS)
Your App = Python Flask backend (needs server)

Solution: Use Render (free Python hosting)

================================================================================
AFTER DEPLOYMENT
================================================================================

Your app will be live at: https://climatovate-sprint1.onrender.com

Test:
- Dashboard loads
- Enroll farmers
- Generate alerts
- Add feedback

Then share with your team and start testing!

================================================================================
NEED HELP?
================================================================================

1. Read DEPLOY_NOW.md for quick guide
2. Read DEPLOYMENT.md for detailed instructions
3. Check DEPLOYMENT_CHECKLIST.md for step-by-step
4. Review Render documentation at render.com/docs

================================================================================
