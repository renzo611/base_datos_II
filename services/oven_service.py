from typing import List, Optional
from database.mongo_db import mongo_client
from models.oven_db import Oven

class OvenService:
    def create_oven(self, oven: Oven):
        mongo_client.ovens.insert_one(oven.__dict__)

    def get_oven(self, oven_id: str) -> Optional[dict]:
        return mongo_client.ovens.find_one({"_id": oven_id})

    def list_ovens(self) -> List[dict]:
        result = list(mongo_client.ovens.find())
        return [{ "id": oven._id, "name": oven.name } for oven in result]
    
    def delete_oven(self, oven_id: str):
        return mongo_client.ovens.delete_one({"_id": oven_id})

