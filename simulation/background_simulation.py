import time
import threading

from integration.event_bus import EventBus
from integration.events import CONSTELLATION_UPDATED
from integration.event_handlers import (
    constellation_updated_handler
)

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

from simulation.position_update_service import (
    PositionUpdateService
)

from simulation.scheduler.simulation_clock import (
    SimulationClock
)

def simulation_loop():

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

    event_bus = EventBus()

    event_bus.subscribe(
        CONSTELLATION_UPDATED,
        constellation_updated_handler
    )

    propagator = OrbitPropagator()

    position_service = (
        PositionUpdateService(
            constellation_manager,
            propagator,
            event_bus
        )
    )

    clock = (
        SimulationClock(
            position_service
        )
    )

    while True:

        clock.tick()

        time.sleep(5)

def start_background_simulation():

    thread = threading.Thread(
        target=simulation_loop,
        daemon=True
    )

    thread.start()

    print(
        "[SIMULATION] Background thread started"
    )