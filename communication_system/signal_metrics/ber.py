import math


def db_to_linear(snr_db):

    return 10 ** (snr_db / 10)


def calculate_ber(snr_db):

    snr_linear = db_to_linear(snr_db)

    ber = 0.5 * math.erfc(
        math.sqrt(snr_linear)
    )

    return ber

def classify_ber(ber):

    if ber < 1e-6:
        return "Excellent"

    elif ber < 1e-4:
        return "Good"

    elif ber < 1e-2:
        return "Fair"

    else:
        return "Poor"