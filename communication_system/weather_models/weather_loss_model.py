
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from communication_system.weather_models.rain_fade import (
    calculate_rain_fade
)


def total_weather_loss(
    weather_condition
):

    return calculate_rain_fade(
        weather_condition
    )