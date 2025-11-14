import requests
from typing import Dict, Any, List
from datetime import datetime, timedelta
import config

class WeatherAPIClient:
    def __init__(self):
        self.api_key = config.WEATHER_API_KEY
        self.base_url = config.WEATHER_API_BASE_URL
    
    def get_hyperlocal_forecast(self, lat: float, lon: float, days: int = 3) -> Dict[str, Any]:
        """
        Query Tomorrow.io API for hyperlocal forecast
        Returns forecast data with hourly rain and heat information
        """
        endpoint = f"{self.base_url}/timelines"
        
        params = {
            'location': f"{lat},{lon}",
            'fields': ['precipitationIntensity', 'temperature', 'humidity'],
            'timesteps': '1h',
            'units': 'metric',
            'apikey': self.api_key
        }
        
        # Set time range for next N days
        start_time = datetime.utcnow()
        end_time = start_time + timedelta(days=days)
        params['startTime'] = start_time.isoformat() + 'Z'
        params['endTime'] = end_time.isoformat() + 'Z'
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return self._parse_response(response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(f"Weather API request failed: {str(e)}")
    
    def _parse_response(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse Tomorrow.io response into standardized format"""
        if 'data' not in raw_data or 'timelines' not in raw_data['data']:
            raise ValueError("Invalid API response format")
        
        timeline = raw_data['data']['timelines'][0]
        intervals = timeline['intervals']
        
        parsed_data = {
            'location': {
                'lat': None,
                'lon': None
            },
            'forecast': []
        }
        
        for interval in intervals:
            time = interval['startTime']
            values = interval['values']
            
            parsed_data['forecast'].append({
                'timestamp': time,
                'precipitation_mm': values.get('precipitationIntensity', 0),
                'temperature_c': values.get('temperature', 0),
                'humidity': values.get('humidity', 0)
            })
        
        return parsed_data

weather_api_client = WeatherAPIClient()
