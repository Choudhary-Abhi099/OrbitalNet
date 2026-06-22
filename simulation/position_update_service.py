from integration.events import (
    CONSTELLATION_UPDATED
)


class PositionUpdateService:

    def __init__(
        self,
        constellation_manager,
        propagator,
        event_bus
    ):

        self.constellation_manager = (
            constellation_manager
        )

        self.propagator = (
            propagator
        )

        self.event_bus = (
            event_bus
        )

    def update_all_positions(self):

        satellites = (
            self.constellation_manager
            .get_all_satellites()
        )

        for satellite in satellites:

            self.propagator.update_position(
                satellite
            )

        self.event_bus.publish(
            CONSTELLATION_UPDATED,
            {
                "constellation_manager":
                self.constellation_manager
            }
        )