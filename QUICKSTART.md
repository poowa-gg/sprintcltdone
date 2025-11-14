# Quick Start Guide - Sprint 1

## ✅ Setup Complete!

Your Climatovate Farmer Weather Alert System is ready to use.

## 🚀 Common Commands

### 1. Query Weather Forecast
Test the weather API for any location (Lagos coordinates shown):
```bash
python src\cli.py forecast query 6.5244 3.3792
```

### 2. Enroll Farmers
Add farmers to your test group (max 10 for Sprint 1):
```bash
python src\cli.py farmer enroll "+2348012345678" 6.5244 3.3792
python src\cli.py farmer enroll "+2348087654321" 9.0820 8.6753
```

### 3. List All Farmers
View all enrolled farmers:
```bash
python src\cli.py farmer list
```

### 4. Generate Alerts
Check all farmers and generate alerts if thresholds are exceeded:
```bash
python src\cli.py alert generate
```

**Alert Thresholds:**
- Heavy Rain: ≥30mm in 3 hours
- Heat Stress: Heat index ≥40

### 5. Review Pending Alerts
See all alerts that need to be sent:
```bash
python src\cli.py alert review
```

### 6. Mark Alert as Delivered
After manually sending SMS/WhatsApp, mark it delivered:
```bash
python src\cli.py alert mark-delivered <alert_id>
```

### 7. Record Farmer Feedback
Collect feedback from farmers:
```bash
python src\cli.py feedback add <farmer_id> "Your feedback text" --cost-saving
```

### 8. View All Feedback
See collected feedback and cost-saving count:
```bash
python src\cli.py feedback list
```

## 📊 Sprint 1 Success Metrics

Track these metrics for PMF validation:

1. **Data Accuracy**: 75% accuracy on 48-hour rain forecasts
2. **Throughput**: Deliver alerts to 10 test farmers over 7 days
3. **Cost-Saving**: Collect 3+ pieces of qualitative feedback confirming cost savings

## 🌍 Sample Nigerian Farm Locations

Use these coordinates for testing:

- **Lagos (Ikorodu)**: 6.6186, 3.5105
- **Ogun (Abeokuta)**: 7.1475, 3.3619
- **Oyo (Ibadan)**: 7.3775, 3.9470
- **Kano**: 12.0022, 8.5919
- **Kaduna**: 10.5105, 7.4165
- **Plateau (Jos)**: 9.8965, 8.8583
- **Benue (Makurdi)**: 7.7336, 8.5240
- **Delta (Warri)**: 5.5160, 5.7500
- **Rivers (Port Harcourt)**: 4.8156, 7.0498
- **Enugu**: 6.5244, 7.5105

## 💡 Daily Workflow

1. **Morning**: Run `alert generate` to check for new conditions
2. **Review**: Use `alert review` to see pending alerts
3. **Send**: Manually send SMS/WhatsApp to farmers
4. **Track**: Mark alerts as delivered with `mark-delivered`
5. **Collect**: Record farmer feedback after 24-48 hours

## 🔧 Troubleshooting

**Weather API Error (401 Unauthorized)**:
- Check your `.env` file has the correct `WEATHER_API_KEY`
- Verify your Tomorrow.io API key is active

**Firestore Error**:
- Ensure `FIREBASE_CONFIG` path in `.env` points to your service account JSON
- Check Firebase project has Firestore enabled

**No Alerts Generated**:
- Current weather may not exceed thresholds
- Try different locations or wait for weather changes
- Thresholds: 30mm/3hrs rain or heat index ≥40

## 📝 Next Steps for Sprint 2

- Automate alert delivery via Twilio/WhatsApp API
- Build web dashboard for analysts
- Add batch processing for larger farmer groups
- Implement caching for repeated queries
- Add multi-language support
