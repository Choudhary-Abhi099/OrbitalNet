from communication_system.communication_engine.node import Node

from communication_system.communication_engine.communication_engine import (
    CommunicationEngine
)


def test_engine():

    ground = Node(
        "Ground",
        28.6139,
        77.2090,
        0
    )

    sat1 = Node(
        "SAT-1",
        28.6139,
        77.2090,
        550
    )

    sat2 = Node(
        "SAT-2",
        29.0,
        78.0,
        550
    )

    engine = CommunicationEngine(
        [ground, sat1, sat2]
    )

    links = engine.build_network()

    print(links)

    assert len(links) == 3


if __name__ == "__main__":

    test_engine()

    print(
        "✅ test_communication_engine passed"
    )