# this is the network service file and contains the services in the network related 

class NetworkStatisticsService:

    def build_statistics(
        self,
        graph
    ):

        satellites = (
            graph.number_of_nodes()
        )

        links = (
            graph.number_of_edges()
        )

        avg_degree = (
            2 * links
        ) / satellites

        return {
            "satellites": satellites,
            "links": links,
            "average_degree": round(
                avg_degree,
                2
            )
        }
    
    
   