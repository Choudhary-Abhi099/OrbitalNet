class SimulationClock:

    def __init__(
        self,
        position_service
    ):

        self.current_time = 0

        self.position_service = (
            position_service
        )

    def tick(self):

        self.current_time += 1

        self.position_service.update_all_positions()

        print(
            f"[CLOCK] Tick "
            f"{self.current_time}"
        )