from typing import Optional
from models.real_butch_data_db import RealTimeBatchData
from database.redis_db import redis_client

class RealTimeBatchDataService:
    def update_data(self, data: RealTimeBatchData):
        redis_client.hmset(f"batch:{data.batch_id}", data.__dict__)

    def get_data(self, batch_id: str) -> Optional[dict]:
        return redis_client.hgetall(f"batch:{batch_id}")