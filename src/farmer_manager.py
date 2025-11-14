from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime
from firestore_service import firestore_service
import uuid

@dataclass
class Farmer:
    farmer_id: str
    phone_number: str
    lat: float
    lon: float
    enrollment_date: str

class FarmerManager:
    def validate_coordinates(self, lat: float, lon: float) -> bool:
        """Validate latitude and longitude ranges"""
        return -90 <= lat <= 90 and -180 <= lon <= 180
    
    def enroll_farmer(self, phone_number: str, lat: float, lon: float) -> str:
        """Enroll a new farmer and return farmer_id"""
        if not self.validate_coordinates(lat, lon):
            raise ValueError(f"Invalid coordinates: lat={lat}, lon={lon}")
        
        farmer_id = str(uuid.uuid4())
        farmer_data = {
            'farmer_id': farmer_id,
            'phone_number': phone_number,
            'lat': lat,
            'lon': lon,
            'enrollment_date': datetime.utcnow().isoformat()
        }
        
        firestore_service.add_document('farmers', farmer_data)
        return farmer_id
    
    def get_all_farmers(self) -> List[Farmer]:
        """Retrieve all enrolled farmers"""
        docs = firestore_service.query_collection('farmers')
        farmers = []
        for doc in docs:
            # Remove 'id' field if present (added by Firestore)
            doc.pop('id', None)
            farmers.append(Farmer(**doc))
        return farmers
    
    def get_farmer(self, farmer_id: str) -> Farmer:
        """Get a specific farmer by ID"""
        doc = firestore_service.get_document('farmers', farmer_id)
        if not doc:
            raise ValueError(f"Farmer not found: {farmer_id}")
        return Farmer(**doc)

farmer_manager = FarmerManager()
