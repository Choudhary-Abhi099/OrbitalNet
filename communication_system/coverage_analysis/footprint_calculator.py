# footprint_calculator.py

import math

from communication_system.coverage_analysis.coverage_radius import (
    calculate_coverage_radius
)


def calculate_footprint(
    satellite_altitude,
    min_elevation_angle=25.0
):
    """
    Calculate satellite footprint.

    Parameters
    ----------
    satellite_altitude : float
        Altitude above Earth (km)

    min_elevation_angle : float
        Minimum elevation angle (degrees)

    Returns
    -------
    dict
    """

    radius = calculate_coverage_radius(
        satellite_altitude,
        min_elevation_angle
    )

    area = math.pi * radius**2

    return {
        "radius_km": radius,
        "area_km2": area
    }