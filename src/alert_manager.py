from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime
from firestore_service import firestore_service
from farmer_manager import Farmer, farmer_manager
from weather_api import weather_api_client
from threshold_evaluator import threshold_evaluator, AlertCondition
import uuid

@dataclass
class Alert:
    alert_id: str
    farmer_id: str
    peril_type: str
    severity: float
    forecast_time: str
    message: str
    generated_at: str
    delivered: bool
    delivered_at: str = None

class AlertManager:
    def generate_alerts_for_all_farmers(self) -> List[Alert]:
        """Generate alerts for all enrolled farmers"""
        farmers = farmer_manager.get_all_farmers()
        all_alerts = []
        
        for farmer in farmers:
            try:
                forecast = weather_api_client.get_hyperlocal_forecast(farmer.lat, farmer.lon)
                conditions = threshold_evaluator.evaluate_forecast(forecast)
                
                for condition in conditions:
                    alert = self._create_alert(farmer, condition)
                    all_alerts.append(alert)
            except Exception as e:
                print(f"Error generating alert for farmer {farmer.farmer_id}: {str(e)}")
        
        return all_alerts
    
    def _create_alert(self, farmer: Farmer, condition: AlertCondition) -> Alert:
        """Create and store an alert"""
        alert_id = str(uuid.uuid4())
        message = self.format_alert_message(farmer, condition)
        
        alert_data = {
            'alert_id': alert_id,
            'farmer_id': farmer.farmer_id,
            'peril_type': condition.peril_type,
            'severity': condition.severity,
            'forecast_time': condition.timestamp,
            'message': message,
            'generated_at': datetime.utcnow().isoformat(),
            'delivered': False
        }
        
        firestore_service.add_document('alerts', alert_data)
        return Alert(**alert_data)
    
    def format_alert_message(self, farmer: Farmer, condition: AlertCondition) -> str:
        """Format alert message for SMS/WhatsApp"""
        if condition.peril_type == 'rain':
            emoji = '🌧️'
            title = 'HEAVY RAIN ALERT'
            action = 'Action: Delay fertilizer application'
        else:
            emoji = '🌡️'
            title = 'HEAT STRESS ALERT'
            action = 'Action: Avoid spraying during peak heat'
        
        message = f"""{emoji} {title}
Location: {farmer.lat:.4f}, {farmer.lon:.4f}
{condition.description}
Time: {condition.timestamp}
{action}"""
        
        return message
    
    def get_pending_alerts(self) -> List[Alert]:
        """Get all undelivered alerts"""
        docs = firestore_service.query_collection('alerts', [('delivered', '==', False)])
        return [Alert(**doc) for doc in docs]
    
    def mark_alert_delivered(self, alert_id: str) -> None:
        """Mark an alert as delivered"""
        firestore_service.update_document('alerts', alert_id, {
            'delivered': True,
            'delivered_at': datetime.utcnow().isoformat()
        })

alert_manager = AlertManager()
