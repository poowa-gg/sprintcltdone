# Web Interface Guide

## 🚀 Starting the Web Interface

### Option 1: Using the Batch File (Windows)
```bash
start_web.bat
```

### Option 2: Direct Python Command
```bash
python web_app.py
```

The web interface will start at: **http://localhost:5000**

## 📱 Features

### 1. Dashboard (Home)
- Overview of all metrics
- Quick action buttons
- Sprint 1 success metrics tracker
- Real-time progress monitoring

**Metrics Displayed:**
- Total Farmers Enrolled
- Pending Alerts
- Total Feedback Collected
- Cost-Saving Feedback Count

### 2. Farmers Management
**View All Farmers:**
- List of enrolled farmers with contact details
- Location coordinates
- Enrollment dates

**Enroll New Farmer:**
- Simple form with phone number and GPS coordinates
- Input validation
- Sample Nigerian locations for quick reference

### 3. Alerts Management
**View Pending Alerts:**
- All undelivered alerts
- Alert type (Rain/Heat)
- Severity levels
- Full alert message preview
- One-click delivery marking

**Generate Alerts:**
- Automatically checks all farmers
- Evaluates weather conditions
- Creates alerts for threshold violations

**Alert Thresholds:**
- Heavy Rain: ≥30mm in 3 hours
- Heat Stress: Heat index ≥40

### 4. Feedback Collection
**View All Feedback:**
- Complete feedback history
- Cost-saving indicators
- Farmer details
- Timestamps

**Add New Feedback:**
- Select farmer from dropdown
- Enter feedback text
- Mark as cost-saving (optional)
- Examples provided for guidance

### 5. Weather Forecast Query
**Query Any Location:**
- Enter latitude/longitude
- View 24-hour forecast
- See alert conditions
- Temperature, precipitation, humidity data

**Quick Locations:**
- Pre-configured Nigerian cities
- One-click coordinate filling

## 🎯 Daily Workflow Using Web Interface

### Morning Routine (9:00 AM)
1. Open dashboard to check metrics
2. Click "Generate Alerts" button
3. Review pending alerts in Alerts page
4. Copy alert messages for manual SMS/WhatsApp delivery

### After Sending Alerts
1. Go to Alerts page
2. Click "Mark Delivered" for each sent alert
3. Track delivery status

### Collecting Feedback (24-48 hours after alert)
1. Go to Feedback page
2. Click "Add Feedback"
3. Select farmer from dropdown
4. Enter their response
5. Check "cost-saving" if applicable
6. Submit

### Weekly Review
1. Check Dashboard metrics
2. Verify Sprint 1 targets:
   - 10 farmers enrolled ✓
   - 3+ cost-saving feedback ✓
   - 7 days of alert delivery ✓

## 💡 Tips for Best Results

### Farmer Enrollment
- Use accurate GPS coordinates
- Verify phone numbers in E.164 format (+234...)
- Enroll farmers from diverse locations for better testing

### Alert Delivery
- Review alert messages before sending
- Personalize if needed
- Send via farmer's preferred channel (SMS/WhatsApp)
- Mark as delivered immediately after sending

### Feedback Collection
- Call farmers 24-48 hours after alert
- Ask specific questions:
  - "Did you receive the alert?"
  - "Was it accurate?"
  - "Did it help you make decisions?"
  - "Did it save you money or prevent loss?"
- Record verbatim responses
- Mark cost-saving feedback clearly

## 🔧 Troubleshooting

**Web Interface Won't Start:**
```bash
# Reinstall Flask
pip install flask

# Check if port 5000 is available
# Try different port:
python web_app.py --port 8000
```

**Can't See Farmers/Alerts:**
- Check Firestore connection
- Verify `.env` file configuration
- Ensure Firebase service account has permissions

**Weather API Errors:**
- Verify API key in `.env`
- Check internet connection
- Confirm Tomorrow.io account is active

## 📊 Sprint 1 Success Tracking

Use the Dashboard to monitor:

| Metric | Target | Track Via |
|--------|--------|-----------|
| Farmers Enrolled | 10 | Dashboard stat card |
| Cost-Saving Feedback | 3+ | Dashboard stat card |
| Alert Delivery Days | 7 | Manual tracking |
| Forecast Accuracy | 75% | Compare with ground truth |

## 🎨 Interface Features

- **Responsive Design**: Works on desktop and tablets
- **Color-Coded Stats**: Visual progress indicators
- **Real-Time Updates**: Refresh to see latest data
- **Clean UI**: Easy navigation and clear actions
- **Form Validation**: Prevents invalid data entry

## 📱 Mobile Access

Access from mobile devices on same network:
1. Find your computer's IP address
2. Open browser on mobile
3. Navigate to: `http://[YOUR_IP]:5000`

Example: `http://192.168.1.100:5000`

## 🔐 Security Note

This is a Sprint 1 MVP for testing. For production:
- Add authentication
- Use HTTPS
- Implement rate limiting
- Add user roles and permissions
- Secure API keys properly

## 📞 Support

For issues or questions:
1. Check QUICKSTART.md for CLI alternatives
2. Review error messages in browser console
3. Check terminal output for Python errors
4. Verify all dependencies are installed
