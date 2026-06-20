def calculate_snr(
    received_power_dbm,
    noise_power_dbm
):

    snr = (
        received_power_dbm
        - noise_power_dbm
    )

    return snr

def classify_link_quality(snr_db):

    if snr_db >= 20:
        return "Excellent"

    elif snr_db >= 10:
        return "Good"

    elif snr_db >= 5:
        return "Fair"

    else:
        return "Poor"