from dataclasses import dataclass

@dataclass
class Satellite:
    satellite_id: str

    latitude: float
    longitude: float
    altitude: float

    velocity: float

    health_status: str

    timestamp: float