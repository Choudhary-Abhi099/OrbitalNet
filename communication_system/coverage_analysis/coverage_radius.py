import numpy as np

EARTH_RADIUS_KM = 6371.0


def calculate_coverage_radius(
    satellite_altitude,
    min_elevation_angle=25.0
):
    """
    Calculate satellite coverage radius on Earth surface.

    Parameters
    ----------
    satellite_altitude : float
        Altitude above Earth in km

    min_elevation_angle : float
        Minimum acceptable elevation angle in degrees

    Returns
    -------
    float
        Coverage radius in km
    """

    R = EARTH_RADIUS_KM
    h = satellite_altitude
    e = np.radians(min_elevation_angle)

    term = (R / (R + h)) * np.cos(e)

    term = np.clip(term, -1.0, 1.0)

    central_angle = np.arccos(term)

    coverage_radius = R * central_angle

    return coverage_radius