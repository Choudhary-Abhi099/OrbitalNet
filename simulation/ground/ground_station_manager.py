from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class GroundStationManager:

    def __init__(self):

        self.ground_stations = {}

        self.distance_calculator = (
            DistanceCalculator()
        )

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

    def get_nearest_station(
        self,
        satellite
    ):

        nearest_station = None

        nearest_distance = (
            float("inf")
        )

        for station in (
            self.ground_stations
            .values()
        ):

            distance = (
                self.distance_calculator
                .calculate_distance(
                    satellite,
                    station
                )
            )

            if distance < nearest_distance:

                nearest_distance = (
                    distance
                )

                nearest_station = (
                    station
                )

        return nearest_station