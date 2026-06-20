# test_rssi_estimator.py

from communication_system.propagation_engine.rssi_estimator import (
    estimate_rssi
)


def test_rssi():

    rssi = estimate_rssi(
        transmit_power_dbm=40,
        transmit_gain_dbi=30,
        receive_gain_dbi=25,
        total_loss_db=121
    )

    assert rssi < 0
    assert rssi > -100


if __name__ == "__main__":
    test_rssi()
    print("✅ test_rssi passed")