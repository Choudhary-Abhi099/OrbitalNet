class ConstellationManager:

    def __init__(self):
        self.satellites = {}

    def add_satellite(self, satellite):
        self.satellites[satellite.satellite_id] = satellite

    def get_satellite(self, satellite_id):
        return self.satellites.get(satellite_id)

    def get_all_satellites(self):
        return list(self.satellites.values())

    def satellite_count(self):
        return len(self.satellites)