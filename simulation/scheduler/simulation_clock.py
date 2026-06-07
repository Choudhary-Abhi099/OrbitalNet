class SimulationClock:

    def __init__(self):
        self.current_time = 0

    def tick(self):
        self.current_time += 1