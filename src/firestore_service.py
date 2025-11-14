import firebase_admin
from firebase_admin import credentials, firestore
from typing import Dict, List, Any, Optional
from datetime import datetime
import config

class FirestoreService:
    def __init__(self):
        self.db = None
        self.initialized = False
    
    def initialize(self):
        if not self.initialized:
            cred = credentials.Certificate(config.FIREBASE_CONFIG)
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.initialized = True
    
    def _get_collection_path(self, collection_name: str) -> str:
        return f"artifacts/{config.APP_ID}/users/{config.USER_ID}/{collection_name}"
    
    def add_document(self, collection_name: str, data: Dict[str, Any]) -> str:
        self.initialize()
        collection_path = self._get_collection_path(collection_name)
        doc_ref = self.db.collection(collection_path).document()
        doc_ref.set(data)
        return doc_ref.id
    
    def get_document(self, collection_name: str, doc_id: str) -> Optional[Dict[str, Any]]:
        self.initialize()
        collection_path = self._get_collection_path(collection_name)
        doc = self.db.collection(collection_path).document(doc_id).get()
        return doc.to_dict() if doc.exists else None
    
    def query_collection(self, collection_name: str, filters: Optional[List] = None) -> List[Dict[str, Any]]:
        self.initialize()
        collection_path = self._get_collection_path(collection_name)
        query = self.db.collection(collection_path)
        
        if filters:
            for field, op, value in filters:
                query = query.where(field, op, value)
        
        docs = query.stream()
        return [{'id': doc.id, **doc.to_dict()} for doc in docs]
    
    def update_document(self, collection_name: str, doc_id: str, data: Dict[str, Any]) -> None:
        self.initialize()
        collection_path = self._get_collection_path(collection_name)
        self.db.collection(collection_path).document(doc_id).update(data)

# Singleton instance
firestore_service = FirestoreService()
