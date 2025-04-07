from datetime import datetime


class GasConsumptionData:
    def __init__(self, timestamp: datetime, flow_rate: float, total_consumed: float):
        self.timestamp = timestamp
        self.flow_rate = flow_rate
        self.total_consumed = total_consumed
