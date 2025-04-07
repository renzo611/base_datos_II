from typing import List, Optional
from models.drying_data_db import DryingData
from models.gas_consumation_db import GasConsumptionData
from models.nut_batch_db import NutBatch
from database.mongo_db import mongo_client
from models.oven_db import Oven

class OvenService:
    def create_oven(self, oven: Oven):
        mongo_client.ovens.insert_one(oven.__dict__)

    def get_oven(self, oven_id: str) -> Optional[dict]:
        return mongo_client.ovens.find_one({"oven_id": oven_id})

    def list_ovens(self) -> List[dict]:
        return list(mongo_client.ovens.find())

class NutBatchService:
    def create_batch(self, batch: NutBatch):
        mongo_client.batches.insert_one(batch.__dict__)

    def get_batch(self, batch_id: str) -> Optional[dict]:
        return mongo_client.batches.find_one({"batch_id": batch_id})

    def list_batches(self) -> List[dict]:
        return list(mongo_client.batches.find())

    def add_drying_data(self, batch_id: str, data: DryingData):
        mongo_client.batches.update_one(
            {"batch_id": batch_id},
            {"$push": {"drying_history": data.__dict__}}
        )

    def add_gas_data(self, batch_id: str, data: GasConsumptionData):
        mongo_client.batches.update_one(
            {"batch_id": batch_id},
            {"$push": {"gas_history": data.__dict__}}
        )
