class TopologyService:

    def build_topology(
        self,
        graph
    ):

        nodes = []

        for node in graph.nodes():

            nodes.append({
                "id": node
            })

        links = []

        for source, target in graph.edges():

            links.append({
                "source": source,
                "target": target
            })

        return {
            "nodes": nodes,
            "links": links
        }