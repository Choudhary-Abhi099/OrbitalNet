from communication_system.telemetry_analysis.outage_detector import (
    get_link_status
)

print(
    get_link_status(
        snr_db=21,
        ber=1e-8
    )
)

print(
    get_link_status(
        snr_db=3,
        ber=1e-8
    )
)

print(
    get_link_status(
        snr_db=21,
        ber=0.05
    )
)