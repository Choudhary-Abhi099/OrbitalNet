from communication_system.coverage_analysis.footprint_calculator import (
    calculate_footprint
)


def generate_service_area(
    satellite_id,
    latitude,
    longitude,
    altitude,
    min_elevation_angle=25.0
):
    """
    Generate service area information.

    Parameters
    ----------
    satellite_id : str
    latitude : float
    longitude : float
    altitude : float
    min_elevation_angle : float

    Returns
    -------
    dict
    """

    footprint = calculate_footprint(
        altitude,
        min_elevation_angle
    )

    return {
        "satellite_id": satellite_id,
        "center_lat": latitude,
        "center_lon": longitude,
        "coverage_radius_km":
            footprint["radius_km"],
        "coverage_area_km2":
            footprint["area_km2"]
    }