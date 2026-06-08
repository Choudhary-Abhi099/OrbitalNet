from communication_system.communication_engine.node import Node
from communication_system.communication_engine.communication_range import calculate_distance

satellite = Node(
    id="SAT-1",
    latitude=28.0,
    longitude=77.0,
    altitude_km=550
)

user = Node(
    id="USER-1",
    latitude=29.0,
    longitude=78.0,
    altitude_km=0
)

distance = calculate_distance(satellite, user)

print(f"Distance: {distance:.2f} km")