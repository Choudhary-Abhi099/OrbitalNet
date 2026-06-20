from communication_system.telemetry_analysis.signal_history import (
    SignalHistory
)

history = SignalHistory()

history.add_record(
    rssi=-79,
    snr=21,
    ber=1e-8
)

history.add_record(
    rssi=-85,
    snr=15,
    ber=1e-5
)

for record in history.get_history():

    print(record)