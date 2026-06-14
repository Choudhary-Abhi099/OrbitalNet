# using the dijikstra algo for this purpose. if there is a better algo implement it later
import networkx as nx


class ShortestPathRouter:

    def find_path(
        self,
        graph,
        source,
        destination
    ):

        try:

            path = nx.shortest_path(
                graph,
                source=source,
                target=destination,
                weight="distance_km"
            )

            total_distance = nx.shortest_path_length(
                graph,
                source=source,
                target=destination,
                weight="distance_km"
            )

            return {
                "path": path,
                "distance_km": total_distance
            }

        except nx.NetworkXNoPath:

            return None