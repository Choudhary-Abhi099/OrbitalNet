def estimate_rssi(
    transmit_power_dbm,
    transmit_gain_dbi,
    receive_gain_dbi,
    total_loss_db
):
    """
    Estimate received signal strength.

    Parameters
    ----------
    transmit_power_dbm : float

    transmit_gain_dbi : float

    receive_gain_dbi : float

    total_loss_db : float

    Returns
    -------
    float
        RSSI in dBm
    """

    rssi_dbm = (
        transmit_power_dbm
        + transmit_gain_dbi
        + receive_gain_dbi
        - total_loss_db
    )

    return rssi_dbm