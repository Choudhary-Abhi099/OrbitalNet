RAIN_ATTENUATION = {
    "clear": 0,
    "light": 2,
    "moderate": 5,
    "heavy": 10,
    "storm": 20
}


def calculate_rain_fade(
    weather_condition
):

    return RAIN_ATTENUATION.get(
        weather_condition.lower(),
        0
    )