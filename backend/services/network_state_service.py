class NetworkStateService:

    def __init__(self):

        self.graph = None

    def update_graph(
        self,
        graph
    ):

        self.graph = graph

    def get_graph(self):

        return self.graph
    
network_state_service = (
    NetworkStateService()
)