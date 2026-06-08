from communication_system.communication_engine.communication_range import (
    calculate_distance
)

from communication_system.coverage_analysis.coverage_radius import (
    calculate_coverage_radius
)


def is_visible(satellite, user):

    distance = calculate_distance(
        satellite,
        user
    )

    coverage_radius = calculate_coverage_radius(
        satellite.altitude_km
    )

    return distance <= coverage_radius