import time
from simulation.scheduler.simulation_clock import SimulationClock
from simulation.orbital.tle_loader import TLELoader
from simulation.orbital.satellite_factory import SatelliteFactory
from simulation.orbital.constellation_manager import ConstellationManager
from simulation.orbital.orbit_propagator import OrbitPropagator
from simulation.routing.graph_builder import GraphBuilder
from simulation.routing.shortest_path import (ShortestPathRouter) 
from simulation.users.user_terminal import (UserTerminal)
from simulation.routing.best_satellite_selector import (BestSatelliteSelector)
from simulation.routing.handover import (HandoverManager)
from simulation.routing.user_connection_manager import (UserConnectionManager)
from simulation.users.user_generator import (UserGenerator)
from simulation.ground.ground_station_generator import (GroundStationGenerator)
from simulation.routing.best_ground_station_selector import (BestGroundStationSelector)
from simulation.routing.end_to_end_route import (EndToEndRouter)
from analytics.route_statics import (RouteStatistics)
from simulation.routing.load_balancer import (LoadBalancer)
 #------------Code Line -----------------
def run_real_constellation():

    clock = SimulationClock()

    loader = TLELoader()

    factory = SatelliteFactory()

    constellation_manager = ConstellationManager()

    propagator = OrbitPropagator()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    satellites = factory.create_satellites(records)

    for satellite in satellites:
        constellation_manager.add_satellite(satellite)

    print(
        f"\nOrbitalNet Started "
        f"({constellation_manager.satellite_count()} satellites loaded)\n"
    )

    MAX_TICKS = 10

    while clock.current_time < MAX_TICKS:

        clock.tick()

        print(
            f"\n===== SIMULATION TIME: "
            f"{clock.current_time} ====="
        )

        for satellite in constellation_manager.get_all_satellites():

            propagator.update_position(
                satellite
            )

            print(
                f"{satellite.satellite_id} | "
                f"Lat: {satellite.latitude:.4f} | "
                f"Lon: {satellite.longitude:.4f} | "
                f"Alt: {satellite.altitude_km:.2f} km"
            )

        time.sleep(1)

    print("\nSimulation Complete.")

# --------- inplementing the graph builder------------#
def test_graph_builder():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    # Update real positions
    for satellite in satellites:

        propagator.update_position(
            satellite
        )

        print(
            f"{satellite.satellite_id} | "
            f"Lat={satellite.latitude:.4f} | "
            f"Lon={satellite.longitude:.4f}"
        )

    graph_builder = GraphBuilder()

    graph = graph_builder.build_graph(
        satellites
    )

    print("\nGraph Nodes:\n")

    for node in graph.nodes:
        print(node)

    print("\nGraph Edges:\n")

    for edge in graph.edges(data=True):
        print(edge)

# ---------Shortest Path trace ---------# 
def test_shortest_path():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    for satellite in satellites:
        propagator.update_position(
            satellite
        )

    graph_builder = GraphBuilder()

    graph = graph_builder.build_graph(
        satellites
    )

    print("\nNodes:")
    print(list(graph.nodes))

    print("\nEdges:")
    print(list(graph.edges(data=True)))

    nodes = list(graph.nodes)

    if len(nodes) < 2:
        print("Need at least 2 satellites")
        return

    source = nodes[0]
    destination = nodes[-1]

    router = ShortestPathRouter()

    result = router.find_path(
        graph,
        source,
        destination
    )

    print("\nRoute Result:")
    print(result)

#---------- BEst nearest satellite -------------
def test_best_satellite_selector():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    for satellite in satellites:

        propagator.update_position(
            satellite
        )

    user = UserTerminal(
        user_id="USER-001",
        latitude=28.6139,
        longitude=77.2090
    )

    selector = BestSatelliteSelector()

    best_satellite = (
        selector.select_best_satellite(
            user,
            satellites
        )
    )

    print("\nUser:")

    print(
        f"{user.user_id} "
        f"({user.latitude}, {user.longitude})"
    )

    print("\nSelected Satellite:")

    print(best_satellite)

# -------------- handover testing ------------
def test_handover():

    handover_manager = (
        HandoverManager()
    )

    current_distance = 1200

    candidate_distance = 900

    result = (
        handover_manager.should_handover(
            current_distance,
            candidate_distance
        )
    )

    print(
        f"Handover Required: {result}"
    )

# --------------- connection -------------
def test_connection_manager():

    manager = UserConnectionManager()

    manager.connect_user(
        "USER-001",
        "NOAA 15"
    )

    print(
        "Initial Connection:",
        manager.get_connected_satellite(
            "USER-001"
        )
    )

    manager.perform_handover(
        "USER-001",
        "ISS (ZARYA)"
    )

    print(
        "After Handover:",
        manager.get_connected_satellite(
            "USER-001"
        )
    )    

# -------- dynamical connectivity ----------
def test_dynamic_connectivity():

    clock = SimulationClock()

    loader = TLELoader()

    factory = SatelliteFactory()

    propagator = OrbitPropagator()

    selector = BestSatelliteSelector()

    handover_manager = HandoverManager()

    connection_manager = UserConnectionManager()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    satellites = factory.create_satellites(
        records
    )

    user = UserTerminal(
        user_id="USER-001",
        latitude=28.6139,
        longitude=77.2090
    )

    MAX_TICKS = 20

    while clock.current_time < MAX_TICKS:

        clock.tick()

        print(
            f"\n===== TIME {clock.current_time} ====="
        )

        # Update all satellite positions
        for satellite in satellites:

            propagator.update_position(
                satellite
            )

        # Find best satellite
        result = (
            selector.select_best_satellite(
                user,
                satellites
            )
        )

        best_satellite = result["satellite"]
        best_distance = result["distance_KM"]

        current_satellite = (
            connection_manager
            .get_connected_satellite(
                user.user_id
            )
        )

        # First connection
        if current_satellite is None:

            connection_manager.connect_user(
                user.user_id,
                best_satellite.satellite_id
            )

            print(
                f"CONNECTED -> "
                f"{best_satellite.satellite_id}"
            )

            continue

        # Handover logic
        if current_satellite != best_satellite.satellite_id:

            print(
                f"Current: {current_satellite}"
            )

            print(
                f"Candidate: "
                f"{best_satellite.satellite_id}"
            )

            connection_manager.perform_handover(
                user.user_id,
                best_satellite.satellite_id
            )

            print("HANDOVER EXECUTED")

        print(
            f"Connected To: "
            f"{connection_manager.get_connected_satellite(user.user_id)}"
        )

        print(
            f"Distance: "
            f"{best_distance:.2f} km"
        )

# ------------- multiple User testing -------------
def test_multiple_users():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    for satellite in satellites:

        propagator.update_position(
            satellite
        )

    generator = UserGenerator()

    users = generator.generate_users()

    selector = BestSatelliteSelector()

    print("\nUser Connections\n")

    for user in users:

        result = (
            selector.select_best_satellite(
                user,
                satellites
            )
        )

        print(
            f"{user.user_id}"
            f" -> "
            f"{result['satellite'].satellite_id}"
            f" | Distance: "
            f"{result['distance_KM']:.2f} km"
        )

# ----------- ground test ------------
def test_ground_station_selection():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    for satellite in satellites:

        propagator.update_position(
            satellite
        )

    station_generator = (
        GroundStationGenerator()
    )

    stations = (
        station_generator.generate_stations()
    )

    selector = (
        BestGroundStationSelector()
    )

    print("\nGround Station Selection\n")

    for satellite in satellites:

        result = (
            selector.select_best_station(
                satellite,
                stations
            )
        )

        print(
            f"{satellite.satellite_id}"
            f" -> "
            f"{result['station'].station_id}"
            f" | Distance: "
            f"{result['distance_km']:.2f} km"
        )


def test_end_to_end_routes():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = factory.create_satellites(
        records
    )

    propagator = OrbitPropagator()

    for satellite in satellites:

        propagator.update_position(
            satellite
        )

    users = (
        UserGenerator()
        .generate_users()
    )

    stations = (
        GroundStationGenerator()
        .generate_stations()
    )

    satellite_selector = (
        BestSatelliteSelector()
    )

    ground_selector = (
        BestGroundStationSelector()
    )

    router = EndToEndRouter()

    routes = []

    print("\n===== END TO END ROUTES =====\n")

    for user in users:

        satellite_result = (
            satellite_selector
            .select_best_satellite(
                user,
                satellites
            )
        )

        ground_station_result = (
            ground_selector
            .select_best_station(
                satellite_result["satellite"],
                stations
            )
        )

        route = (
            router.build_route(
                user,
                satellite_result,
                ground_station_result
            )
        )

        routes.append(route)

        print(route)

    stats = RouteStatistics()

    print("\n===== SATELLITE USAGE =====\n")

    satellite_usage = (
        stats.satellite_usage(
            routes
        )
    )
    load_balancer = LoadBalancer()
    most_loaded = (load_balancer.find_most_loaded_satellite(satellite_usage))
    least_loaded = (load_balancer.find_least_loaded_satellite(satellite_usage))

    print(f"\nMost Loaded Satellite: "f"{most_loaded}")
    print(f"Least Loaded Satellite: "f"{least_loaded}")
    for satellite, count in satellite_usage.items():

        print(
            f"{satellite}: {count} users"
        )

    print("\n===== GROUND STATION USAGE =====\n")

    station_usage = (
        stats.ground_station_usage(
            routes
        )
    )

    for station, count in station_usage.items():

        print(
            f"{station}: {count} users"
        )

def main():
    # run_real_constellation()
    test_end_to_end_routes()

if __name__ == "__main__":
    main()