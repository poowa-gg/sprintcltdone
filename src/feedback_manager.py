from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime
from firestore_service import firestore_service
import uuid

@dataclass
class Feedback:
    feedback_id: str
    farmer_id: str
    feedback_text: str
    cost_saving_indicator: bool
    feedback_date: str

class FeedbackManager:
    def record_feedback(self, farmer_id: str, feedback_text: str, cost_saving: bool = False) -> str:
        """Record farmer feedback and return feedback_id"""
        feedback_id = str(uuid.uuid4())
        feedback_data = {
            'feedback_id': feedback_id,
            'farmer_id': farmer_id,
            'feedback_text': feedback_text,
            'cost_saving_indicator': cost_saving,
            'feedback_date': datetime.utcnow().isoformat()
        }
        
        firestore_service.add_document('feedback', feedback_data)
        return feedback_id
    
    def get_all_feedback(self) -> List[Feedback]:
        """Retrieve all feedback records"""
        docs = firestore_service.query_collection('feedback')
        feedbacks = []
        for doc in docs:
            doc.pop('id', None)
            feedbacks.append(Feedback(**doc))
        return feedbacks
    
    def get_farmer_feedback(self, farmer_id: str) -> List[Feedback]:
        """Get feedback for a specific farmer"""
        docs = firestore_service.query_collection('feedback', [('farmer_id', '==', farmer_id)])
        feedbacks = []
        for doc in docs:
            doc.pop('id', None)
            feedbacks.append(Feedback(**doc))
        return feedbacks

feedback_manager = FeedbackManager()
