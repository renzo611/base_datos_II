from datetime import datetime


class DryingData:
    def __init__(self, timestamp: datetime, temperature: float, humidity: float, weight: float, gas_consumption: float):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.weight = weight
        self.gas_consumption = gas_consumption
