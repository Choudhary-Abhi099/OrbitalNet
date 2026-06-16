from simulation.routing.shortest_path import (
    ShortestPathRouter
)


class SatelliteRouteManager:

    def __init__(self):

        self.router = (
            ShortestPathRouter()
        )

    def build_route(
        self,
        graph,
        source_satellite,
        destination_satellite
    ):

        return self.router.find_path(
            graph,
            source_satellite,
            destination_satellite
        )