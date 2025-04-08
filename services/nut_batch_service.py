from typing import List, Optional

from bson import ObjectId
from models.drying_data_db import DryingData
from models.nut_batch_db import NutBatch, NutStatus
from database.mongo_db import mongo_client

class NutBatchService:
    def create_batch(self, batch: NutBatch):
        try:
            real_batch = mongo_client.batches.find_one({"oven_id": batch.oven_id, "status": NutStatus.IN_PROGRESS.value})
        
            if real_batch:
                raise Exception("Existe una batch en este horno sin completar, por favor finaliza la accion de secado")
            
            mongo_client.batches.insert_one(batch.__dict__)
        except Exception as e:
            print("Excepcion", e)

    def get_batch(self, batch_id: str) -> Optional[dict]:
        batch = mongo_client.batches.find_one({"_id": ObjectId(batch_id)})
        if batch is None:
            raise Exception("Este lote no existe")

    def list_batches(self) -> List[dict]:
        return list(mongo_client.batches.find())
    
    def get_actual_batch_by_oven(self,oven_id: str):
        print('entro')
        batch = mongo_client.batches.find_one({"oven_id": oven_id, "status": NutStatus.IN_PROGRESS.value})

        if batch is None:
                raise Exception("No existe un lote en este horno sin completar, por favor registra un lote para esta accion")
        
        return batch

    def add_drying_data(self, oven_id: str, data: DryingData):
        real_batch = mongo_client.batches.find_one({"oven_id": oven_id, "status": NutStatus.IN_PROGRESS.value})

        if real_batch is None:
                raise Exception("No existe un lote en este horno sin completar, por favor registra un lote para esta accion")
        


        mongo_client.batches.update_one(
            {"oven_id": oven_id},
            {"$push": {"drying_history": data.__dict__}}
        )