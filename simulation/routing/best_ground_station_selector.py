from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class BestGroundStationSelector:

    def __init__(self):

        self.distance_calculator = (
            DistanceCalculator()
        )

    def select_best_station(
        self,
        satellite,
        stations
    ):

        best_station = None

        best_distance = float("inf")

        for station in stations:

            distance = (
                self.distance_calculator
                .calculate_distance(
                    satellite,
                    station
                )
            )

            if distance < best_distance:

                best_distance = distance

                best_station = station

        return {
            "station": best_station,
            "distance_km": best_distance
        }