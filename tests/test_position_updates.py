import time

from integration.event_bus import EventBus

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

from integration.events import (
    CONSTELLATION_UPDATED
)

from integration.event_handlers import (
    constellation_updated_handler
)
def test_position_updates():

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

    event_bus.subscribe(
        CONSTELLATION_UPDATED,
        constellation_updated_handler
    )

    satellite = (
        constellation_manager
        .get_satellite(
            "SCD 1"
        )
    )

    position_service = (
        PositionUpdateService(
            constellation_manager,
            propagator,
            event_bus
        )
    )

    print("\nUpdate 1:")

    position_service.update_all_positions()

    print(
        satellite.satellite_id,
        satellite.latitude,
        satellite.longitude,
        satellite.altitude_km
    )

    time.sleep(5)

    print("\nUpdate 2:")

    position_service.update_all_positions()

    print(
        satellite.satellite_id,
        satellite.latitude,
        satellite.longitude,
        satellite.altitude_km
    )


if __name__ == "__main__":

    test_position_updates()