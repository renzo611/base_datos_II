from datetime import datetime
from typing import Optional


class Oven:
    def __init__(self, oven_id: str, name: str, location: Optional[str] = None):
        self.oven_id = oven_id
        self.name = name
        self.location = location
        self.created_at = datetime.now()