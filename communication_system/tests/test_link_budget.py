from communication_system.link_budget.link_budget import (
    calculate_received_power
)

received_power = calculate_received_power(
    transmit_power_dbm=40,
    tx_gain_dbi=30,
    rx_gain_dbi=25,
    path_loss_db=174,
    misc_losses_db=0
)

print(
    f"Received Power = {received_power:.2f} dBm"
)
