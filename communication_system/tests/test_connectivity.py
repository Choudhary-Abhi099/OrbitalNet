from communication_system.communication_engine.node import Node
from communication_system.communication_engine.connectivity_validator import is_link_available

satellite = Node(
    id="SAT-1",
    latitude=28,
    longitude=77,
    altitude_km=550
)

user = Node(
    id="USER-1",
    latitude=29,
    longitude=78,
    altitude_km=0
)

print(
    is_link_available(
        satellite,
        user
    )
)