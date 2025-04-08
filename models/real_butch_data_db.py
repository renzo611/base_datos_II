from datetime import datetime


class RealTimeBatchData:
    def __init__(self, batch_id: str, temperature: float, humidity: float, weight: float, gas_consumption: float, oven_id: str):
        self.batch_id = batch_id
        self.oven_id = oven_id
        self.temperature = temperature
        self.humidity = humidity
        self.weight = weight
        self.gas_consumption = gas_consumption
        self.timestamp = datetime.now().isoformat()
