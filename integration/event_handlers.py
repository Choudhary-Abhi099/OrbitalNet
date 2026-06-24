import asyncio
from integration.routing_adapter import (
    RoutingAdapter
)
from integration.telemetry_adapter import (
    TelemetryAdapter
)
from simulation.routing.graph_builder import (
    GraphBuilder
)
from backend.services.network_state_service import (
    network_state_service
)

from backend.websocket.connection_manager import (
    manager
)

from backend.services.live_stats_service import (
    live_stats_service
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

    network_state_service.update_graph(
        graph
    )
    stats = {

        "network": {

            "satellites":
            graph.number_of_nodes(),

            "links":
            graph.number_of_edges(),

            "average_degree":
            round(
                (
                    2 * graph.number_of_edges()
                ) /
                graph.number_of_nodes(),
                2
            )
        },

        "connectivity": {

            "user_id":
            "user-1",

            "connected_satellite":
            "SCD 1",

            "ground_station":
            "GS-DELHI",

            "status":
            "CONNECTED"
        },

        "communication": {

            "status":
            "ONLINE",

            "rssi":
            -79,

            "snr":
            21,

            "latency":
            2.1,

            "packet_loss":
            0.1
        }
    }


    live_stats_service.update(
        stats
    )

    print(
        f"[ROUTING] Graph rebuilt "
        f"Nodes={graph.number_of_nodes()} "
        f"Links={graph.number_of_edges()}"
    )