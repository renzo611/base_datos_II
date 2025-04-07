from datetime import datetime


class RealTimeGasData:
    def __init__(self, oven_id: str, flow_rate: float, total_consumed: float):
        self.oven_id = oven_id
        self.flow_rate = flow_rate
        self.total_consumed = total_consumed
        self.timestamp = datetime.now().isoformat()
