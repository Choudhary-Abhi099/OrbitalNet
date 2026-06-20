def calculate_received_power(
    transmit_power_dbm,
    tx_gain_dbi,
    rx_gain_dbi,
    path_loss_db,
    misc_losses_db=0
):

    received_power = (
        transmit_power_dbm
        + tx_gain_dbi
        + rx_gain_dbi
        - path_loss_db
        - misc_losses_db
    )

    return received_power