# Modelos en Python para MongoDB y Redis
from datetime import datetime
from typing import List

from models.drying_data_db import DryingData

class NutBatch:
    def __init__(self, nut_type: str, initial_weight: float, target_humidity: float, oven_id: str):
        self.nut_type = nut_type
        self.start_date = datetime.now()
        self.end_date = None
        self.initial_weight = initial_weight
        self.target_humidity = target_humidity
        self.oven_id = oven_id
        self.drying_history: List[DryingData] = []
        self.status = "In Progress"

