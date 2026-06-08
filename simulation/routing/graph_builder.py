import networkx as nx

# this is the function that calculates the neighbour nodes (i.e statellites that are closer to each other)
class GraphBuilder:

    def __init__(self):
        self.graph = nx.Graph()

    def build_graph(self, satellites):

        self.graph.clear()

        for satellite in satellites:

            self.graph.add_node(
                satellite.satellite_id
            )

        return self.graph