from simulation.orbital.tle_loader import TLELoader
from simulation.orbital.satellite_factory import SatelliteFactory
from simulation.orbital.orbit_propagator import OrbitPropagator
from simulation.routing.graph_builder import GraphBuilder


class NetworkStateService:

    def get_graph(self):

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

        propagator = OrbitPropagator()

        for satellite in satellites:

            propagator.update_position(
                satellite
            )

        graph_builder = GraphBuilder()

        return graph_builder.build_graph(
            satellites
        )