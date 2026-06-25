class GroundStationStateService:

    def __init__(self):

        self.manager = None

    def update(
        self,
        manager
    ):

        self.manager = manager

    def get_manager(self):

        return self.manager


ground_station_state_service = (
    GroundStationStateService()
)