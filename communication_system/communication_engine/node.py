from dataclasses import dataclass

@dataclass
class Node:
    id: str
    latitude: float
    longitude: float
    altitude_km: float