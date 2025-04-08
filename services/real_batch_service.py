import json
from typing import List
from models.real_butch_data_db import RealTimeBatchData
from database.redis_db import redis_client

class RealTimeBatchDataService:
    def update_data(self, data: RealTimeBatchData):
        redis_client.rpush(f"batch_history:{data.batch_id}", json.dumps(data.__dict__))

    def get_all_data(self, batch_id: str) -> List[dict]:
        data_list = redis_client.lrange(f"batch_history:{batch_id}", 0, -1)
        return [json.loads(item) for item in data_list]