from communication_system.communication_engine.link_establishment import (
    establish_link
)


class CommunicationEngine:

    def __init__(self, nodes):

        self.nodes = nodes

    def build_network(self):

        active_links = []

        n = len(self.nodes)

        for i in range(n):

            for j in range(i + 1, n):

                result = establish_link(
                    self.nodes[i],
                    self.nodes[j]
                )

                active_links.append(
                    {
                        "node1": self.nodes[i].id,
                        "node2": self.nodes[j].id,
                        "link": result
                    }
                )

        return active_links