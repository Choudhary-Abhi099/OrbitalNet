from communication_system.signal_metrics.latency import (
    calculate_latency
)

latency = calculate_latency(1000)

print(
    f"Latency = {latency:.2f} ms"
)