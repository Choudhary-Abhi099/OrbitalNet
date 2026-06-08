# backend/main.py

import time

from simulation.orbital.satellite import Satellite
from simulation.orbital.constellation_manager import ConstellationManager
from simulation.orbital.orbit_propagator import OrbitPropagator
from simulation.orbital.tle_loader import TLELoader
from simulation.orbital.orbit_propagator import OrbitPropagator
from simulation.scheduler.simulation_clock import SimulationClock


def create_initial_constellation():
    satellites = [
        Satellite(
            satellite_id="SAT-001",
            latitude=0.0,
            longitude=0.0,
            altitude=550.0,
            velocity=1.2,
            health_status="ACTIVE",
            timestamp=0
        ),
        Satellite(
            satellite_id="SAT-002",
            latitude=15.0,
            longitude=20.0,
            altitude=550.0,
            velocity=1.1,
            health_status="ACTIVE",
            timestamp=0
        ),
        Satellite(
            satellite_id="SAT-003",
            latitude=-10.0,
            longitude=40.0,
            altitude=550.0,
            velocity=1.3,
            health_status="ACTIVE",
            timestamp=0
        ),
        Satellite(
            satellite_id="SAT-004",
            latitude=30.0,
            longitude=60.0,
            altitude=550.0,
            velocity=1.0,
            health_status="ACTIVE",
            timestamp=0
        ),
        Satellite(
            satellite_id="SAT-005",
            latitude=-25.0,
            longitude=80.0,
            altitude=550.0,
            velocity=1.4,
            health_status="ACTIVE",
            timestamp=0
        ),
    ]

    return satellites


def run_simulation():

    clock = SimulationClock()

    constellation_manager = ConstellationManager()

    propagator = OrbitPropagator()

    satellites = create_initial_constellation()

    for satellite in satellites:
        constellation_manager.add_satellite(satellite)

    print("OrbitalNet Simulation Started...\n")

    MAX_TICKS = 10

    while clock.current_time < MAX_TICKS:

        clock.tick()

        print(f"\n===== SIMULATION TIME: {clock.current_time} =====")

        for satellite in constellation_manager.get_all_satellites():

            propagator.propagate(
                satellite=satellite,
                delta_time=1
            )

            print(
                f"{satellite.satellite_id} | "
                f"Lat: {satellite.latitude:.2f} | "
                f"Lon: {satellite.longitude:.2f} | "
                f"Alt: {satellite.altitude:.2f} km"
            )

        time.sleep(1)

    print("\nSimulation Complete.")


def test_tle_loader():

    loader = TLELoader()

    satellites = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    print("\nLoaded TLE Satellites:\n")

    for satellite in satellites:
        print(satellite)
        print("-" * 60)


def test_orbit_propagator():

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    propagator = OrbitPropagator()

    print("\nCurrent Satellite Positions\n")

    for record in records:

        position = propagator.get_position(record)

        print(position)

def main():
     test_orbit_propagator()
    # test_tle_loader()
    # use run simulator in case for the test_tle_loader
    # run_simulation()  


if __name__ == "__main__":
    main()