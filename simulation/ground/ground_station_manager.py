class GroundStationManager:

    def __init__(self):

        self.ground_stations = {}

    def add_station(
        self,
        station
    ):

        self.ground_stations[
            station.station_id
        ] = station

    def get_all_stations(self):

        return list(
            self.ground_stations.values()
        )