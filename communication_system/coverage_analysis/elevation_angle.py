import numpy as np


def calculate_elevation_angle(
    satellite_position,
    ground_station_position
):
    """
    Calculate elevation angle between a satellite
    and ground station.

    Parameters
    ----------
    satellite_position : tuple
        (x, y, z) in km

    ground_station_position : tuple
        (x, y, z) in km

    Returns
    -------
    float
        Elevation angle in degrees
    """

    sat = np.array(satellite_position, dtype=float)
    gs = np.array(ground_station_position, dtype=float)

    los = sat - gs

    los_unit = los / np.linalg.norm(los)

    zenith_unit = gs / np.linalg.norm(gs)

    angle_deg = np.degrees(
        np.arccos(
            np.clip(
                np.dot(los_unit, zenith_unit),
                -1.0,
                1.0
            )
        )
    )

    elevation = 90.0 - angle_deg

    return elevation