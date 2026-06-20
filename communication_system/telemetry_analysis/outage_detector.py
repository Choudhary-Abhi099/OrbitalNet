def detect_outage(
    snr_db,
    ber
):

    if snr_db < 5:
        return True

    if ber > 0.01:
        return True

    return False

def get_link_status(
    snr_db,
    ber
):

    outage = detect_outage(
        snr_db,
        ber
    )

    if outage:
        return "OUTAGE"

    return "ONLINE"