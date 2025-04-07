from datetime import datetime
from typing import Optional


class Oven:
    def __init__(self, name: str, location: Optional[str] = None):
        self.name = name
        self.location = location
        self.created_at = datetime.now()