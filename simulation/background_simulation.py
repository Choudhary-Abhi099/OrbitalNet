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
from backend.services.constellation_state_service import (
    constellation_state_service
)

from backend.services.route_state_service import (
    route_state_service
)

from simulation.users.user_generator import (
    UserGenerator
)

from simulation.routing.best_satellite_selector import (
    BestSatelliteSelector
)

from simulation.ground.ground_station_generator import (
    GroundStationGenerator
)

from simulation.routing.best_ground_station_selector import (
    BestGroundStationSelector
)

from simulation.routing.end_to_end_route import (
    EndToEndRouter
)

from backend.services.orbit_path_state_service import (
    orbit_path_service
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
    constellation_state_service.update(
        constellation_manager
    )
    event_bus = EventBus()

    event_bus.subscribe(
        CONSTELLATION_UPDATED,
        constellation_updated_handler
    )

    propagator = OrbitPropagator()
    
    for satellite in satellites:

        orbit_path_service.generate_path(
            satellite,
            propagator
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

    router = (
        EndToEndRouter()
    )
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
        routes = []

        for user in users:

            satellite_result = (
                satellite_selector
                .select_best_satellite(
                    user,
                    constellation_manager
                    .get_all_satellites()
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

        route_state_service.update(
            routes
        )
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