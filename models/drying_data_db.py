from datetime import datetime


class DryingData:
    def __init__(self, timestamp: datetime, temperature: float, humidity: float, weight: float, gas_consumption: float):
        self.timestamp = timestamp
        self.final_temperature = temperature
        self.final_humidity = humidity
        self.final_weight = weight
        self.total_gas_consumption = gas_consumption
