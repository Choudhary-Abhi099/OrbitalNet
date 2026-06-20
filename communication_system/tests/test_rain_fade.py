from communication_system.weather_models.rain_fade import (
    calculate_rain_fade
)

for weather in [
    "clear",
    "light",
    "moderate",
    "heavy",
    "storm"
]:

    loss = calculate_rain_fade(
        weather
    )

    print(
        f"{weather}: {loss} dB"
    )