# Design Document

## Overview

The Farmer Weather Alert System is a Python-based CLI application that integrates with third-party weather APIs to deliver hyperlocal forecasts to farmers. Sprint 1 focuses on manual operations with a simple command-line interface for Climatovate analysts to verify data, manage farmer enrollments, generate alerts, and collect feedback.

## Architecture

### System Components

- **CLI Interface**: Command-line entry point for all analyst operations
- **Weather API Client**: Integrates with Tomorrow.io or similar hyperlocal weather API
- **Threshold Evaluator**: Analyzes forecast data against alert thresholds
- **Farmer Manager**: Handles farmer enrollment and data validation
- **Alert Manager**: Generates and tracks alert messages
- **Feedback Manager**: Records and retrieves farmer feedback
- **Firestore Service**: Database abstraction layer

### Technology Stack


- **Language**: Python 3.9+
- **Database**: Google Firestore
- **Weather API**: Tomorrow.io (configurable)
- **CLI Framework**: Click
- **HTTP Client**: requests
- **Firebase SDK**: firebase-admin

## Data Models

### Firestore Collections

**Collection Path**: `/artifacts/{app_id}/users/{user_id}/farmers`

**Farmer Document**:
```json
{
  "farmer_id": "string (auto-generated UUID)",
  "phone_number": "string (E.164 format)",
  "lat": "float (-90 to 90)",
  "lon": "float (-180 to 180)",
  "enrollment_date": "timestamp"
}
```

**Collection Path**: `/artifacts/{app_id}/users/{user_id}/alerts`

**Alert Document**:
```json
{
  "alert_id": "string (auto-generated UUID)",
  "farmer_id": "string (reference)",
  "peril_type": "string (rain|heat)",
  "severity": "float",
  "forecast_time": "timestamp",
  "message": "string",
  "generated_at": "timestamp",
  "delivered": "boolean",
  "delivered_at": "timestamp (optional)"
}
```

**Collection Path**: `/artifacts/{app_id}/users/{user_id}/feedback`

**Feedback Document**:
```json
{
  "feedback_id": "string (auto-generated UUID)",
  "farmer_id": "string (reference)",
  "feedback_text": "string",
  "cost_saving_indicator": "boolean",
  "feedback_date": "timestamp"
}
```

## Components

### 1. CLI Interface (`cli.py`)

Commands:
- `forecast query <lat> <lon>` - Query weather API
- `farmer enroll <phone> <lat> <lon>` - Add farmer
- `farmer list` - View all farmers
- `alert generate` - Generate alerts for all farmers
- `alert review` - Display pending alerts
- `alert mark-delivered <alert_id>` - Mark alert as sent
- `feedback add <farmer_id> <text> [--cost-saving]` - Record feedback
- `feedback list` - View all feedback

### 2. Weather API Client (`weather_api.py`)

```python
class WeatherAPIClient:
    def get_hyperlocal_forecast(
        lat: float, 
        lon: float, 
        days: int = 3
    ) -> Dict[str, Any]
```

Returns forecast with hourly rain and heat data for 72 hours.

### 3. Threshold Evaluator (`threshold_evaluator.py`)

```python
class ThresholdEvaluator:
    HEAVY_RAIN_THRESHOLD = 30  # mm in 3 hours
    HEAT_STRESS_THRESHOLD = 40
    
    def evaluate_forecast(
        forecast_data: Dict[str, Any]
    ) -> List[AlertCondition]
```

### 4. Farmer Manager (`farmer_manager.py`)

```python
class FarmerManager:
    def enroll_farmer(phone: str, lat: float, lon: float) -> str
    def get_all_farmers() -> List[Farmer]
    def validate_coordinates(lat: float, lon: float) -> bool
```

### 5. Alert Manager (`alert_manager.py`)

```python
class AlertManager:
    def generate_alerts_for_all_farmers() -> List[Alert]
    def format_alert_message(farmer: Farmer, conditions: List) -> str
    def get_pending_alerts() -> List[Alert]
    def mark_alert_delivered(alert_id: str) -> None
```

Alert message format:
```
🌧️ HEAVY RAIN ALERT
Location: [lat], [lon]
Expected: [amount]mm in next 48hrs
Time: [date/time]
Action: Delay fertilizer application
```

### 6. Feedback Manager (`feedback_manager.py`)

```python
class FeedbackManager:
    def record_feedback(farmer_id: str, text: str, cost_saving: bool) -> str
    def get_all_feedback() -> List[Feedback]
```

### 7. Firestore Service (`firestore_service.py`)

```python
class FirestoreService:
    def initialize(config: Dict) -> None
    def add_document(collection: str, data: Dict) -> str
    def get_document(collection: str, doc_id: str) -> Dict
    def query_collection(collection: str, filters: List) -> List[Dict]
    def update_document(collection: str, doc_id: str, data: Dict) -> None
```

## Configuration

### Environment Variables

- `WEATHER_API_KEY`: API key for weather service
- `WEATHER_API_BASE_URL`: Base URL (default: Tomorrow.io)
- `FIREBASE_CONFIG`: Path to Firebase service account JSON
- `APP_ID`: Application identifier for Firestore paths
- `USER_ID`: User identifier for Firestore paths

### Firebase Configuration

Service account JSON with Firestore permissions required.

## Error Handling

- API timeouts: 10 second limit, retry once
- Invalid coordinates: Validate before API calls
- Missing API key: Fail fast with clear error message
- Firestore errors: Log and display user-friendly messages
- Network errors: Retry with exponential backoff

## Testing Strategy

- Unit tests for threshold evaluation logic
- Integration tests with mock weather API
- Manual testing with 10 test farmer coordinates
- Validation against ground truth weather data

## Future Considerations

- Automated alert delivery via Twilio/WhatsApp API
- Web dashboard for analysts
- Batch processing for large farmer lists
- Caching layer for repeated location queries
- Multi-language alert messages
