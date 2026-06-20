# snr.py

def calculate_snr(
    received_power_dbm,
    noise_power_dbm
):
    """
    Calculate Signal-to-Noise Ratio.

    Parameters
    ----------
    received_power_dbm : float

    noise_power_dbm : float

    Returns
    -------
    float
        SNR in dB
    """

    return (
        received_power_dbm
        - noise_power_dbm
    )


def classify_link_quality(
    snr_db
):
    """
    Classify communication quality.
    """

    if snr_db >= 20:
        return "Excellent"

    elif snr_db >= 10:
        return "Good"

    elif snr_db >= 5:
        return "Fair"

    return "Poor"