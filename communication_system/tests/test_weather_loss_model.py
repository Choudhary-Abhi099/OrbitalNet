from communication_system.link_budget.link_budget import (
    calculate_received_power
)

from communication_system.weather_models.weather_loss_model import (
    total_weather_loss
)

base_received_power = calculate_received_power(
    transmit_power_dbm=70,
    tx_gain_dbi=30,
    rx_gain_dbi=25,
    path_loss_db=174
)

print(
    f"Clear Sky Received Power: "
    f"{base_received_power:.2f} dBm"
)

for weather in [
    "light",
    "moderate",
    "heavy",
    "storm"
]:

    weather_loss = total_weather_loss(
        weather
    )

    adjusted_power = (
        base_received_power
        - weather_loss
    )

    print(
        f"{weather.capitalize():<10} "
        f"Weather Loss: {weather_loss:>2} dB | "
        f"Received Power: {adjusted_power:.2f} dBm"
    )