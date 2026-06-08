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

    tle_line1: str = ""
    tle_line2: str = ""