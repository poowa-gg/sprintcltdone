# Fix Render Start Command Error

## The Problem

Error: `bash: line 1: web:: command not found`

This means Render is not using the Procfile correctly. It's trying to run the entire line as a bash command.

## The Solution

### Fix the Start Command in Render Dashboard

1. Go to https://dashboard.render.com
2. Click your service: `climatovate-sprint1`
3. Click **"Settings"** (left sidebar)
4. Scroll down to **"Build & Deploy"**
5. Find **"Start Command"**
6. It should say: `gunicorn web_app:app`
7. If it says anything else (like `web: gunicorn web_app:app`), change it to:
   ```
   gunicorn web_app:app
   ```
8. Click **"Save Changes"**

### Manual Redeploy

After saving:
1. Go to **"Manual Deploy"** (top right)
2. Click **"Deploy latest commit"**
3. Wait 5-10 minutes

---

## ✅ Correct Configuration

In Render dashboard, you should have:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn web_app:app
```

**NOT:**
- ❌ `web: gunicorn web_app:app`
- ❌ `python web_app.py`
- ❌ `flask run`

---

## 🔍 Why This Happens

The Procfile format is:
```
web: gunicorn web_app:app
```

But Render's "Start Command" field should only have:
```
gunicorn web_app:app
```

The `web:` part is for Heroku/Procfile, not for Render's start command field.

---

## 📋 Quick Checklist

- [ ] Go to Render dashboard
- [ ] Click Settings
- [ ] Find "Start Command"
- [ ] Change to: `gunicorn web_app:app`
- [ ] Save changes
- [ ] Manual deploy
- [ ] Wait for deployment
- [ ] Check logs

---

Your app should deploy successfully after this fix! 🚀
