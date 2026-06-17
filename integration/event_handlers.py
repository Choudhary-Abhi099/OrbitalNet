from integration.routing_adapter import (
    RoutingAdapter
)
from integration.telemetry_adapter import (
    TelemetryAdapter
)

telemetry_adapter = (
    TelemetryAdapter()
)

routing_adapter = RoutingAdapter()


def satellite_failure_handler(
    data
):

    satellite = data[
        "satellite"
    ]

    print(
        f"\n[EVENT] "
        f"Satellite Failed: "
        f"{satellite.satellite_id}"
    )

    routing_adapter.satellite_failed(
        data
    )
    telemetry_adapter.record_event(
        "SATELLITE_FAILED",
        data
    )