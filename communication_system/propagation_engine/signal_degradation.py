# signal_degradation.py

from communication_system.propagation_engine.fspl import (
    calculate_fspl
)
from communication_system.propagation_engine.attenuation import (
    calculate_attenuation
)


def calculate_total_loss(
    distance_km,
    frequency_ghz,
    weather_loss_db=0.0,
    additional_loss_db=0.0
):
    """
    Calculate total propagation loss.

    Parameters
    ----------
    distance_km : float

    frequency_ghz : float

    weather_loss_db : float

    additional_loss_db : float

    Returns
    -------
    dict
    """

    fspl_db = calculate_fspl(
        distance_km,
        frequency_ghz
    )

    attenuation_db = calculate_attenuation(
        weather_loss_db=weather_loss_db,
        additional_loss_db=additional_loss_db
    )

    total_loss_db = (
        fspl_db
        + attenuation_db
    )

    return {
        "fspl_db": fspl_db,
        "weather_loss_db": weather_loss_db,
        "additional_loss_db": additional_loss_db,
        "total_loss_db": total_loss_db
    }