# Modelos en Python para MongoDB y Redis
from datetime import datetime
from enum import Enum
from typing import List

from models.drying_data_db import DryingData

class NutStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class NutType(str, Enum):
    HALF = "HALF"
    BUTTERFLY = "BUTTERFLY" 

class NutBatch:
    def __init__(self, nut_type: NutType, initial_weight: float, target_humidity: float, initial_humidity: float, oven_id: str):
        self.nut_type = nut_type.value
        self.start_date = datetime.now()
        self.end_date = None
        self.initial_weight = initial_weight
        self.initial_humidity = initial_humidity
        self.target_humidity = target_humidity
        self.oven_id = oven_id
        self.drying_history: List[DryingData] = []
        self.status = NutStatus.IN_PROGRESS.value

