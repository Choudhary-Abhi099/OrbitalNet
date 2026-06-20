SPEED_OF_LIGHT = 299792  # km/s


def calculate_latency(distance_km):

    latency_seconds = (
        distance_km /
        SPEED_OF_LIGHT
    )

    latency_ms = (
        latency_seconds * 1000
    )

    return latency_ms