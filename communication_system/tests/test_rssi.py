from communication_system.signal_metrics.rssi import (
    calculate_rssi,
    classify_rssi
)

rssi = calculate_rssi(-79)

quality = classify_rssi(rssi)

print(f"RSSI = {rssi:.2f} dBm")
print(f"Quality = {quality}")