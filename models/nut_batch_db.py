# Modelos en Python para MongoDB y Redis
from datetime import datetime
from typing import List

from models.drying_data_db import DryingData
from models.gas_consumation_db import GasConsumptionData

class NutBatch:
    def __init__(self, batch_id: str, nut_type: str, initial_weight: float, target_humidity: float, oven_id: str):
        self.batch_id = batch_id
        self.nut_type = nut_type
        self.start_date = datetime.now()
        self.initial_weight = initial_weight
        self.target_humidity = target_humidity
        self.oven_id = oven_id
        self.drying_history: List[DryingData] = []
        self.gas_history: List[GasConsumptionData] = []
        self.status = "In Progress"

