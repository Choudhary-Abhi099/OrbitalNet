import math


def calculate_fspl(
    distance_km,
    frequency_ghz
):
    """
    Calculate Free Space Path Loss.

    Parameters
    ----------
    distance_km : float
        Distance between transmitter and receiver

    frequency_ghz : float
        Carrier frequency

    Returns
    -------
    float
        FSPL in dB
    """

    if distance_km <= 0:
        raise ValueError(
            "Distance must be positive"
        )

    if frequency_ghz <= 0:
        raise ValueError(
            "Frequency must be positive"
        )

    fspl_db = (
        20 * math.log10(distance_km)
        + 20 * math.log10(frequency_ghz)
        + 92.45
    )

    return fspl_db