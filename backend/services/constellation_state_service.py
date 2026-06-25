class ConstellationStateService:

    def __init__(self):

        self.constellation_manager = None

    def update(
        self,
        constellation_manager
    ):

        self.constellation_manager = (
            constellation_manager
        )

    def get_constellation(self):

        return (
            self.constellation_manager
        )


constellation_state_service = (
    ConstellationStateService()
)