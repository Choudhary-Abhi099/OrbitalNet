import math

EARTH_RADIUS = 6371  # km


def calculate_coverage_radius(altitude_km):

    radius = math.sqrt(
        (EARTH_RADIUS + altitude_km) ** 2
        - EARTH_RADIUS ** 2
    )

    return radius