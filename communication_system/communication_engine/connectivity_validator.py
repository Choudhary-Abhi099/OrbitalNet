from communication_system.communication_engine.communication_range import calculate_distance

MAX_LINK_DISTANCE = 2000  # km


def is_link_available(node1, node2):

    distance = calculate_distance(node1, node2)

    return distance <= MAX_LINK_DISTANCE