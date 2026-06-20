import math


def calculate_fspl(distance_km, frequency_mhz):

    fspl = (
        20 * math.log10(distance_km)
        + 20 * math.log10(frequency_mhz)
        + 32.44
    )

    return fspl