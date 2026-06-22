from integration.routing_adapter import (
    RoutingAdapter
)
from integration.telemetry_adapter import (
    TelemetryAdapter
)
from simulation.routing.graph_builder import (
    GraphBuilder
)

graph_builder = GraphBuilder()
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

def low_snr_handler(data):

    satellite_id = data[
        "satellite_id"
    ]

    snr = data[
        "snr"
    ]

    print(
        f"\n[EVENT] "
        f"LOW SNR: "
        f"{satellite_id} "
        f"(SNR={snr})"
    )

    telemetry_adapter.record_event(
        "LOW_SNR",
        data
    )

def link_down_handler(data):

    satellite_id = data[
        "satellite_id"
    ]

    print(
        f"\n[EVENT] "
        f"LINK DOWN: "
        f"{satellite_id}"
    )

    telemetry_adapter.record_event(
        "LINK_DOWN",
        data
    )

def link_recovered_handler(data):

    satellite_id = data[
        "satellite_id"
    ]

    print(
        f"\n[EVENT] "
        f"LINK RECOVERED: "
        f"{satellite_id}"
    )

    telemetry_adapter.record_event(
        "LINK_RECOVERED",
        data
    )

def satellite_position_updated_handler(
        data
    ):

        satellite = data[
        "satellite"
        ]

        print(
            f"[POSITION UPDATED] "
            f"{satellite.satellite_id}"
        )

def constellation_updated_handler(
    data
):

    constellation_manager = data[
        "constellation_manager"
    ]

    satellites = (
        constellation_manager
        .get_all_satellites()
    )

    graph = (
        graph_builder
        .build_graph(
            satellites
        )
    )

    print(
        f"[ROUTING] Graph rebuilt "
        f"Nodes={graph.number_of_nodes()} "
        f"Links={graph.number_of_edges()}"
    )