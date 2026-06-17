from dataclasses import dataclass
from datetime import datetime


@dataclass
class TelemetryEvent:

    event_type: str
    timestamp: datetime
    description: str