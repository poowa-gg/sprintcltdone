# Render Environment Variables - Exact Values

## 📋 Copy and Paste These Exactly

When Render asks for "Name" and "Value", add these **6 variables** one by one:

---

### Variable 1: Weather API Key

**Name (Key):**
```
WEATHER_API_KEY
```

**Value:**
```
6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD
```

---

### Variable 2: Weather API Base URL

**Name (Key):**
```
WEATHER_API_BASE_URL
```

**Value:**
```
https://api.tomorrow.io/v4
```

---

### Variable 3: App ID

**Name (Key):**
```
APP_ID
```

**Value:**
```
climatovate
```

---

### Variable 4: User ID

**Name (Key):**
```
USER_ID
```

**Value:**
```
admin
```

---

### Variable 5: Secret Key

**Name (Key):**
```
SECRET_KEY
```

**Value:**
```
climatovate-production-secret-2024
```

---

### Variable 6: Firebase Config (IMPORTANT!)

**Name (Key):**
```
FIREBASE_CONFIG_BASE64
```

**Value:**
Open the file `firebase_base64.txt` in your project folder and copy **ALL** the content (it's one very long line). Paste it here.

**How to get the value:**
1. Open `firebase_base64.txt` (it's in your project folder)
2. Press `Ctrl+A` to select all
3. Press `Ctrl+C` to copy
4. Paste into Render's "Value" field

The value should start with: `ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOi...`

---

## ✅ Checklist

Add these variables in Render:

- [ ] WEATHER_API_KEY = `6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD`
- [ ] WEATHER_API_BASE_URL = `https://api.tomorrow.io/v4`
- [ ] APP_ID = `climatovate`
- [ ] USER_ID = `admin`
- [ ] SECRET_KEY = `climatovate-production-secret-2024`
- [ ] FIREBASE_CONFIG_BASE64 = (content from firebase_base64.txt)

---

## 🎯 Step-by-Step in Render

1. In Render, when creating your web service, scroll down to **"Environment Variables"**
2. Click **"Add Environment Variable"**
3. For each variable above:
   - Enter the **Name** in the "Key" field
   - Enter the **Value** in the "Value" field
   - Click **"Add"** or press Enter
4. Repeat for all 6 variables
5. Then click **"Create Web Service"**

---

## ⚠️ Common Mistakes to Avoid

❌ **Don't add quotes** around the values
- Wrong: `"climatovate"`
- Right: `climatovate`

❌ **Don't add spaces** before or after
- Wrong: ` climatovate `
- Right: `climatovate`

❌ **Don't copy only part** of FIREBASE_CONFIG_BASE64
- Must copy the ENTIRE content from firebase_base64.txt
- It should be one very long line (1000+ characters)

✅ **Copy exactly** as shown above

---

## 🆘 If You Get Errors

**"WEATHER_API_KEY not found"**
- Check spelling: `WEATHER_API_KEY` (all caps, underscores)
- Make sure value is: `6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD`

**"FIREBASE_CONFIG not found"**
- Check spelling: `FIREBASE_CONFIG_BASE64` (not just FIREBASE_CONFIG)
- Make sure you copied ALL content from firebase_base64.txt
- Value should be very long (1000+ characters)

**"Invalid Firebase config"**
- Open firebase_base64.txt
- Make sure you copied the entire line
- No extra spaces or line breaks

---

## 📸 Visual Guide

```
┌─────────────────────────────────────────┐
│ Add Environment Variable                │
├─────────────────────────────────────────┤
│ Key:   WEATHER_API_KEY                  │
│ Value: 6v6mO3wXjWWhDA4BXw85XgLkZhLhcgmD │
│                                         │
│ [Add Environment Variable]              │
└─────────────────────────────────────────┘
```

Repeat this 6 times for each variable!

---

## ✅ After Adding All Variables

You should see all 6 variables listed:
1. WEATHER_API_KEY
2. WEATHER_API_BASE_URL
3. APP_ID
4. USER_ID
5. SECRET_KEY
6. FIREBASE_CONFIG_BASE64

Then click **"Create Web Service"** and wait for deployment!

---

Good luck! 🚀
