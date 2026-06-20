from dataclasses import dataclass


@dataclass
class GroundStation:

    station_id: str

    latitude: float
    longitude: float

    status: str = "ACTIVE"