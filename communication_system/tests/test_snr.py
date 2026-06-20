from communication_system.signal_metrics.snr import (
    calculate_snr,
    classify_link_quality
)

snr = calculate_snr(
    received_power_dbm=-79,
    noise_power_dbm=-100
)

quality = classify_link_quality(
    snr
)

print(
    f"SNR = {snr:.2f} dB"
)

print(
    f"Quality = {quality}"
)