import time

from simulation.orbital.tle_loader import (
    TLELoader
)

from simulation.orbital.satellite_factory import (
    SatelliteFactory
)

from simulation.orbital.constellation_manager import (
    ConstellationManager
)

from simulation.orbital.orbit_propagator import (
    OrbitPropagator
)

from simulation.routing.graph_builder import (
    GraphBuilder
)

from simulation.routing.satellite_route_manager import (
    SatelliteRouteManager
)

from integration.event_bus import (
    EventBus
)

from simulation.position_update_service import (
    PositionUpdateService
)


def test_dynamic_routing():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = (
        factory.create_satellites(
            records
        )
    )

    constellation_manager = (
        ConstellationManager()
    )

    for satellite in satellites:

        constellation_manager.add_satellite(
            satellite
        )

    propagator = (
        OrbitPropagator()
    )

    event_bus = (
        EventBus()
    )

    position_service = (
        PositionUpdateService(
            constellation_manager,
            propagator,
            event_bus
        )
    )

    graph_builder = (
        GraphBuilder()
    )

    route_manager = (
        SatelliteRouteManager()
    )
    position_service.update_all_positions()

    satellites = (
        constellation_manager
        .get_all_satellites()
    )

    graph = (
        graph_builder.build_graph(
            satellites
        )
    )

    source = satellites[0]
    destination = satellites[20]

    route1 = (
        route_manager.build_route(
            graph,
            source.satellite_id,
            destination.satellite_id
        )
    )

    print("\n=== Route 1 ===")
    print(route1)

    time.sleep(60)

    position_service.update_all_positions()

    graph = (
        graph_builder.build_graph(
            satellites
        )
    )

    route2 = (
        route_manager.build_route(
            graph,
            source.satellite_id,
            destination.satellite_id
        )
    )

    print("\n=== Route 2 ===")
    print(route2)


if __name__ == "__main__":

    test_dynamic_routing()