class ConstellationManager:

    def __init__(self):
        self.satellites = {}

    def add_satellite(self, satellite):
        self.satellites[satellite.satellite_id] = satellite

    def get_all_satellites(self):
        return self.satellites.values()