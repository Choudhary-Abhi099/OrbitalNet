import networkx as nx

from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class GraphBuilder:

    NEIGHBOR_COUNT = 4

    def __init__(self):

        self.graph = nx.Graph()

        self.distance_calculator = (
            DistanceCalculator()
        )

    def build_graph(self, satellites):

        self.graph.clear()

        # Add nodes
        for satellite in satellites:

            self.graph.add_node(
                satellite.satellite_id,
                satellite=satellite
            )

        # Add edges using nearest neighbors

        for satellite in satellites:

            neighbors = []

            for other_satellite in satellites:

                if satellite == other_satellite:
                    continue

                distance = (
                    self.distance_calculator
                    .calculate_distance(
                        satellite,
                        other_satellite
                    )
                )

                neighbors.append(
                    (
                        other_satellite,
                        distance
                    )
                )

            neighbors.sort(
                key=lambda x: x[1]
            )

            nearest_neighbors = (
                neighbors[:self.NEIGHBOR_COUNT]
            )

            for neighbor, distance in nearest_neighbors:

                self.graph.add_edge(
                    satellite.satellite_id,
                    neighbor.satellite_id,
                    distance_km=distance
                )

        return self.graph

    def get_graph(self):

        return self.graph