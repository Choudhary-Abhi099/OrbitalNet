from communication_system.reports.communication_report import (
    generate_communication_report
)

report = generate_communication_report(
    distance=650,
    fspl=170.3,
    received_power=-79,
    rssi=-79,
    snr=21,
    ber=1e-8,
    latency=2.1,
    packet_loss=0.1,
    status="ONLINE"
)

for key, value in report.items():
    print(f"{key}: {value}")