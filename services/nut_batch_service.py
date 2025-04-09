from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from models.drying_data_db import DryingData
from models.nut_batch_db import NutBatch, NutStatus
from database.mongo_db import mongo_client
from services.real_batch_service import RealTimeBatchDataService

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
        batch = mongo_client.batches.find_one({"oven_id": oven_id, "status": NutStatus.IN_PROGRESS.value})

        if batch is None:
                raise Exception("No existe un lote en este horno sin completar, por favor registra un lote para esta accion")
        
        return batch

    def add_drying_data(self, oven_id: str):
        real_batch = mongo_client.batches.find_one({"oven_id": oven_id, "status": NutStatus.IN_PROGRESS.value})

        if real_batch is None:
                raise Exception("No existe un lote en este horno sin completar, por favor registra un lote para esta accion")
        

        real_batch_service = RealTimeBatchDataService()
        data = real_batch_service.get_all_data(real_batch["_id"])

        if data:
            latest = max(data, key=lambda x: x["timestamp"])
            
            total_gas = sum(item.get("gas_consumption", 0) for item in data)
            
            drying_data = DryingData(
                timestamp=datetime.fromisoformat(latest["timestamp"]),
                temperature=latest["temperature"],
                humidity=latest["humidity"],
                weight=latest["weight"],
                gas_consumption=total_gas
            )
            status = NutStatus.IN_PROGRESS
            if real_batch["target_humidity"] >= latest["humidity"]:
                 status = NutStatus.COMPLETED
            
            return mongo_client.batches.update_one(
                {"_id": real_batch["_id"]},
                {
                    "$set": {
                        "final_drying_values": drying_data.__dict__,
                        "status": status
                    }
                }
            )