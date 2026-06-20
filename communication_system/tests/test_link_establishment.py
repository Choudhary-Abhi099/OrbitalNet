# test_link_establishment.py

from communication_system.communication_engine.node import Node

from communication_system.communication_engine.link_establishment import (
    establish_link
)


def test_link():

    node1 = Node(
        "Ground",
        28.6139,
        77.2090,
        0
    )

    node2 = Node(
        "SAT-1",
        28.6139,
        77.2090,
        550
    )

    result = establish_link(
        node1,
        node2
    )
    print("Node1:", node1)
    print("Node2:", node2)
    print(result)

    assert result["status"] == "Connected"


if __name__ == "__main__":
    print("TEST FILE LOADED")
    test_link()
    print("✅ test_link_establishment passed")