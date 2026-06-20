from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class BestSatelliteSelector:

    def __init__(self):

        self.distance_calculator = (
            DistanceCalculator()
        )

    def select_best_satellite(
        self,
        user,
        satellites
    ):

        best_satellite = None

        best_distance = float("inf")

        for satellite in satellites:

            distance = (
                self.distance_calculator
                .calculate_distance(
                    user,
                    satellite
                )
            )

            if distance < best_distance:

                best_distance = distance

                best_satellite = satellite

        return {
            "satellite" : best_satellite,
            "distance_KM" : best_distance
        }