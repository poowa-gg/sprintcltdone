from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime, timedelta
import config

@dataclass
class AlertCondition:
    peril_type: str
    severity: float
    timestamp: str
    duration_hours: int
    description: str

class ThresholdEvaluator:
    def __init__(self):
        self.heavy_rain_threshold = config.HEAVY_RAIN_THRESHOLD
        self.heat_stress_threshold = config.HEAT_STRESS_THRESHOLD
    
    def evaluate_forecast(self, forecast_data: Dict[str, Any]) -> List[AlertCondition]:
        """
        Analyze forecast data and identify alert conditions
        Returns list of conditions that exceed thresholds within 48 hours
        """
        alerts = []
        forecast = forecast_data.get('forecast', [])
        
        # Check rain conditions (30mm in 3 hours)
        rain_alerts = self._check_rain_conditions(forecast)
        alerts.extend(rain_alerts)
        
        # Check heat conditions
        heat_alerts = self._check_heat_conditions(forecast)
        alerts.extend(heat_alerts)
        
        return alerts
    
    def _check_rain_conditions(self, forecast: List[Dict]) -> List[AlertCondition]:
        """Check for heavy rain (30mm in 3 hours) within 48 hours"""
        alerts = []
        
        # Use 3-hour rolling window
        for i in range(len(forecast) - 2):
            if i >= 48:  # Only check first 48 hours
                break
            
            three_hour_rain = sum([
                forecast[i].get('precipitation_mm', 0),
                forecast[i+1].get('precipitation_mm', 0),
                forecast[i+2].get('precipitation_mm', 0)
            ])
            
            if three_hour_rain >= self.heavy_rain_threshold:
                alerts.append(AlertCondition(
                    peril_type='rain',
                    severity=three_hour_rain,
                    timestamp=forecast[i]['timestamp'],
                    duration_hours=3,
                    description=f"Heavy rain expected: {three_hour_rain:.1f}mm in 3 hours"
                ))
                break  # Only report first occurrence
        
        return alerts
    
    def _check_heat_conditions(self, forecast: List[Dict]) -> List[AlertCondition]:
        """Check for heat stress conditions within 48 hours"""
        alerts = []
        
        for i, hour in enumerate(forecast[:48]):
            temp = hour.get('temperature_c', 0)
            humidity = hour.get('humidity', 0)
            
            # Simple heat index calculation
            heat_index = self._calculate_heat_index(temp, humidity)
            
            if heat_index >= self.heat_stress_threshold:
                alerts.append(AlertCondition(
                    peril_type='heat',
                    severity=heat_index,
                    timestamp=hour['timestamp'],
                    duration_hours=1,
                    description=f"Heat stress expected: index {heat_index:.1f}"
                ))
                break  # Only report first occurrence
        
        return alerts
    
    def _calculate_heat_index(self, temp_c: float, humidity: float) -> float:
        """Simple heat index calculation"""
        # Simplified formula for demonstration
        # In production, use proper heat index calculation
        return temp_c + (humidity / 100) * 5

threshold_evaluator = ThresholdEvaluator()
