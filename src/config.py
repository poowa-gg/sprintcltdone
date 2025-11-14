import os
import base64
import tempfile
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root (for local development)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_BASE_URL = os.getenv('WEATHER_API_BASE_URL', 'https://api.tomorrow.io/v4')
APP_ID = os.getenv('APP_ID', 'climatovate')
USER_ID = os.getenv('USER_ID', 'admin')

# Handle Firebase config (file path or base64 for deployment)
FIREBASE_CONFIG = os.getenv('FIREBASE_CONFIG')
FIREBASE_CONFIG_BASE64 = os.getenv('FIREBASE_CONFIG_BASE64')

if FIREBASE_CONFIG_BASE64 and not FIREBASE_CONFIG:
    # Decode base64 and save temporarily (for cloud deployment)
    try:
        # Add padding if needed
        missing_padding = len(FIREBASE_CONFIG_BASE64) % 4
        if missing_padding:
            FIREBASE_CONFIG_BASE64 += '=' * (4 - missing_padding)
        
        config_json = base64.b64decode(FIREBASE_CONFIG_BASE64).decode('utf-8')
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        temp_file.write(config_json)
        temp_file.close()
        FIREBASE_CONFIG = temp_file.name
    except Exception as e:
        raise ValueError(f"Failed to decode FIREBASE_CONFIG_BASE64: {str(e)}")

# Alert thresholds
HEAVY_RAIN_THRESHOLD = 30  # mm in 3 hours
HEAT_STRESS_THRESHOLD = 40

# Validation
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable is required")
if not FIREBASE_CONFIG:
    raise ValueError("FIREBASE_CONFIG or FIREBASE_CONFIG_BASE64 environment variable is required")
