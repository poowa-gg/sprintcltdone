# GitHub Setup Guide

## Step-by-Step: Push Your Code to GitHub

### Step 1: Check Git Status

```bash
# Check if git is initialized
git status
```

If you see "fatal: not a git repository", initialize it:
```bash
git init
```

### Step 2: Remove Sensitive Files from Tracking

**Important:** Make sure these files are NOT committed:

```bash
# If .env was accidentally added, remove it
git rm --cached .env

# If Firebase JSON was added, remove it
git rm --cached "C:/Users/3CHUB/Downloads/climatovate--mvp1-sprint-firebase-adminsdk-fbsvc-40d0c7999a.json"
```

### Step 3: Add All Files

```bash
git add .
```

### Step 4: Commit Your Code

```bash
git commit -m "Sprint 1 MVP - Farmer Weather Alert System

- Weather API integration (Tomorrow.io)
- Farmer management system
- Alert generation and tracking
- Feedback collection
- Web dashboard interface
- CLI tools
- Firestore database integration"
```

### Step 5: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon (top right) → **"New repository"**
3. Fill in:
   - **Repository name**: `climatovate-sprint1`
   - **Description**: `Hyperlocal weather alert system for farmers - Sprint 1 MVP`
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README (you already have one)
4. Click **"Create repository"**

### Step 6: Connect and Push

GitHub will show you commands. Use these:

```bash
# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/climatovate-sprint1.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

### Step 7: Verify Upload

1. Refresh your GitHub repository page
2. You should see all your files
3. **Check that `.env` and Firebase JSON are NOT there**

---

## 🔒 Security Checklist

Before pushing, verify:

- [ ] `.env` file is in `.gitignore`
- [ ] Firebase service account JSON is in `.gitignore`
- [ ] No API keys in code
- [ ] `.env.example` has placeholder values only
- [ ] Sensitive files removed from git tracking

---

## 📝 Future Updates

When you make changes:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of your changes"

# Push to GitHub
git push
```

---

## 🆘 Common Issues

### "Permission denied (publickey)"

You need to set up SSH keys or use HTTPS with personal access token:

**Option 1: Use HTTPS with Token**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select "repo" scope
4. Copy the token
5. When pushing, use:
   ```bash
   git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/climatovate-sprint1.git
   ```

**Option 2: Use GitHub Desktop**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. Add your local repository
4. Push with one click

### "Failed to push some refs"

Someone else pushed changes. Pull first:
```bash
git pull origin main --rebase
git push
```

### "Large files detected"

GitHub has a 100MB file limit. Check for large files:
```bash
git ls-files -s | sort -k 4 -n -r | head -10
```

Remove large files:
```bash
git rm --cached path/to/large/file
git commit -m "Remove large file"
```

---

## ✅ Next Steps

After pushing to GitHub:
1. ✅ Code is backed up
2. ✅ Version control enabled
3. ✅ Ready for deployment
4. → Go to `DEPLOYMENT.md` for deployment instructions

---

## 🎯 Quick Reference

```bash
# Initialize git
git init

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Your message"

# Add remote
git remote add origin https://github.com/USERNAME/REPO.git

# Push
git push -u origin main

# Future pushes
git push
```
