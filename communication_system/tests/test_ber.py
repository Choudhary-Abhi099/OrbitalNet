from communication_system.signal_metrics.ber import (
    calculate_ber,
    classify_ber
)

ber = calculate_ber(21)

quality = classify_ber(ber)

print(f"BER = {ber:.10e}")
print(f"Quality = {quality}")