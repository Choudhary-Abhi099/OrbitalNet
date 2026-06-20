def calculate_rssi(received_power_dbm):

    return received_power_dbm


def classify_rssi(rssi_dbm):

    if rssi_dbm >= -60:
        return "Excellent"

    elif rssi_dbm >= -75:
        return "Good"

    elif rssi_dbm >= -90:
        return "Fair"

    else:
        return "Poor"