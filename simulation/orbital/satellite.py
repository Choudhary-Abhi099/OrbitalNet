from dataclasses import dataclass

@dataclass
class Satellite:
    satellite_id: str
    latitude: float
    longitude: float
    altitude_km: float
    status: str = "ACTIVE"
    tle_line1: str = ""
    tle_line2: str = ""