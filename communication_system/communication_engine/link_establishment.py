from communication_system.communication_engine.communication_range import (
    calculate_distance
)

from communication_system.communication_engine.connectivity_validator import (
    is_link_available
)


def establish_link(
    node1,
    node2
):
    """
    Establish a communication link
    between two nodes.
    """

    distance = calculate_distance(
        node1,
        node2
    )

    available = is_link_available(
        node1,
        node2
    )

    if available:

        return {
            "status": "Connected",
            "distance_km": distance
        }

    return {
        "status": "Disconnected",
        "distance_km": distance
    }