# RealTimeGasData Service (Redis simulation)
from typing import Optional
from models.real_gas_db import RealTimeGasData
from database.redis_db import redis_client


class RealTimeGasDataService:
    def update_gas(self, data: RealTimeGasData):
        redis_client.hmset(f"oven:{data.oven_id}", data.__dict__)

    def get_gas(self, oven_id: str) -> Optional[dict]:
        return redis_client.hgetall(f"oven:{oven_id}")
