class RouteStateService:

    def __init__(self):
        self.routes = []

    def update(
        self,
        routes
    ):
        self.routes = routes

    def get_routes(self):
        return self.routes


route_state_service = (
    RouteStateService()
)