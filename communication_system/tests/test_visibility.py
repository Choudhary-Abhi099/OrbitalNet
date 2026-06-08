import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from communication_system.communication_engine.node import Node
from communication_system.coverage_analysis.visibility_checker import (
    is_visible
)

satellite = Node(
    id="SAT-1",
    latitude=28,
    longitude=77,
    altitude_km=550
)

user = Node(
    id="USER-1",
    latitude=-45,
    longitude=120,
    altitude_km=0
)

print(
    "Visible:",
    is_visible(
        satellite,
        user
    )
)