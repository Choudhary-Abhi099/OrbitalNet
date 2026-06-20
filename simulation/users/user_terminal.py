from dataclasses import dataclass


@dataclass
class UserTerminal:

    user_id: str

    latitude: float
    longitude: float

    connected_satellite: str = None