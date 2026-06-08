import time

from simulation.scheduler.simulation_clock import SimulationClock

from simulation.orbital.tle_loader import TLELoader
from simulation.orbital.satellite_factory import SatelliteFactory
from simulation.orbital.constellation_manager import ConstellationManager
from simulation.orbital.orbit_propagator import OrbitPropagator
from simulation.routing.graph_builder import GraphBuilder

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

    satellites = factory.create_satellites(records)

    graph_builder = GraphBuilder()

    graph = graph_builder.build_graph(
        satellites
    )

    print("\nGraph Nodes:\n")

    for node in graph.nodes:
        print(node)


def main():
    # run_real_constellation()
    test_graph_builder()

if __name__ == "__main__":
    main()