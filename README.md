# Climatovate Farmer Weather Alert System - Sprint 1

Hyperlocal weather alert system for farmers to optimize agricultural decisions and prevent input waste.

## 🚀 Quick Start

**New to the system?** Start here: [START_HERE.md](START_HERE.md)

**Choose your interface:**
- 🌐 **Web Interface** (Recommended): [WEB_INTERFACE.md](WEB_INTERFACE.md)
- 💻 **Command Line**: [QUICKSTART.md](QUICKSTART.md)

## Features

- Query hyperlocal weather forecasts (1km resolution)
- Enroll farmers with location coordinates
- Generate automated alerts for heavy rain and heat stress
- Manual alert review and delivery tracking
- Collect farmer feedback for PMF validation

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Required variables:
- `WEATHER_API_KEY`: Your Tomorrow.io API key
- `FIREBASE_CONFIG`: Path to Firebase service account JSON
- `APP_ID`: Your application ID (default: climatovate)
- `USER_ID`: Your user ID (default: admin)

### 3. Firebase Setup

1. Create a Firebase project
2. Enable Firestore database
3. Download service account key JSON
4. Update `FIREBASE_CONFIG` path in `.env`

## Usage

### Query Weather Forecast

```bash
python src/cli.py forecast query 40.7128 -74.0060
```

### Enroll a Farmer

```bash
python src/cli.py farmer enroll "+1234567890" 40.7128 -74.0060
```

### List All Farmers

```bash
python src/cli.py farmer list
```

### Generate Alerts

```bash
python src/cli.py alert generate
```

### Review Pending Alerts

```bash
python src/cli.py alert review
```

### Mark Alert as Delivered

```bash
python src/cli.py alert mark-delivered <alert_id>
```

### Record Feedback

```bash
python src/cli.py feedback add <farmer_id> "Saved money by delaying fertilizer" --cost-saving
```

### List All Feedback

```bash
python src/cli.py feedback list
```

## Alert Thresholds

- **Heavy Rain**: ≥30mm in 3 hours
- **Heat Stress**: Heat index ≥40

## Data Structure

### Firestore Collections

- `/artifacts/{app_id}/users/{user_id}/farmers` - Farmer enrollment data
- `/artifacts/{app_id}/users/{user_id}/alerts` - Generated alerts
- `/artifacts/{app_id}/users/{user_id}/feedback` - Farmer feedback

## Sprint 1 Success Metrics

- 75% accuracy on 48-hour rain forecasts
- Successfully deliver alerts to 10 test farmers over 7 days
- Collect 3+ pieces of qualitative cost-saving feedback

## Next Steps

- Automate alert delivery via Twilio/WhatsApp
- Build web dashboard for analysts
- Add batch processing for large farmer lists
- Implement caching for repeated queries
