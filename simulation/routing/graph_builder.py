# this is the function that calculates the neighbour nodes (i.e statellites that are closer to each other) and the 
import networkx as nx

from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class GraphBuilder:

    MAX_ISL_DISTANCE = 20000

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
                satellite = satellite
            )

        # Add edges
        for i in range(len(satellites)):

            for j in range(i + 1, len(satellites)):

                sat1 = satellites[i]
                sat2 = satellites[j]

                distance = (
                    self.distance_calculator
                    .calculate_distance(
                        sat1,
                        sat2
                    )
                )

                if distance <= self.MAX_ISL_DISTANCE:

                    self.graph.add_edge(
                        sat1.satellite_id,
                        sat2.satellite_id,
                        distance_km=distance
                    )

        return self.graph

    def get_graph(self):
        return self.graph