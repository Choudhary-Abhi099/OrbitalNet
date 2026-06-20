# test_signal_degradation.py

from communication_system.propagation_engine.signal_degradation import (
    calculate_total_loss
)


def test_signal_degradation():

    result = calculate_total_loss(
        distance_km=1000,
        frequency_ghz=12,
        weather_loss_db=5,
        additional_loss_db=2
    )

    assert result["total_loss_db"] > result["fspl_db"]


if __name__ == "__main__":
    test_signal_degradation()
    print("✅ test_signal_degradation passed")