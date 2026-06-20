def estimate_packet_loss(snr_db):

    if snr_db >= 20:
        return 0.1

    elif snr_db >= 10:
        return 1

    elif snr_db >= 5:
        return 5

    else:
        return 20