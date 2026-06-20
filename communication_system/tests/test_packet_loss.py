from communication_system.signal_metrics.packet_loss import (
    estimate_packet_loss
)

scenarios = [
    ("Excellent Link", 25),
    ("Good Link", 15),
    ("Fair Link", 8),
    ("Poor Link", 3)
]

for scenario, snr in scenarios:

    packet_loss = estimate_packet_loss(
        snr
    )

    print("-" * 40)

    print(f"Scenario     : {scenario}")
    print(f"SNR          : {snr} dB")
    print(f"Packet Loss  : {packet_loss}%")