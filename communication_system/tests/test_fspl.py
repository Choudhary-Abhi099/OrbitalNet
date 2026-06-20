from communication_system.propagation_engine.fspl import (
    calculate_fspl
)

distance = 1000      # km
frequency = 12000    # MHz (Ku Band)

loss = calculate_fspl(
    distance,
    frequency
)

print(f"FSPL = {loss:.2f} dB")