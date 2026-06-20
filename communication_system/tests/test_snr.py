from communication_system.signal_metrics.snr import (
    calculate_snr,
    classify_link_quality
)


def test_snr():

    snr = calculate_snr(
        received_power_dbm=-30,
        noise_power_dbm=-100
    )

    print("Calculated SNR =", snr)

    assert snr == 70


def test_link_quality():

    quality = classify_link_quality(25)

    print("Link Quality =", quality)

    assert quality == "Excellent"


if __name__ == "__main__":
    test_snr()
    test_link_quality()

    print("✅ test_snr passed")