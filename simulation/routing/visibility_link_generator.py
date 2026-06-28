from simulation.routing.distance_calculator import (
    DistanceCalculator
)


class VisibilityLinkGenerator:

    def __init__(self):
        self.distance_calculator = (
            DistanceCalculator()
        )

    def generate_links(
        self,
        satellites,
        stations
    ):

        links = []

        for station in stations:

            closest_satellite = None
            best_distance = float("inf")

            for satellite in satellites:

                distance = (
                    self.distance_calculator
                    .calculate_distance(
                        station,
                        satellite
                    )
                )

                if distance < best_distance:
                    best_distance = distance
                    closest_satellite = satellite

            if closest_satellite:

                links.append(
                    {
                        "satellite":
                        closest_satellite.satellite_id,

                        "ground_station":
                        station.station_id,

                        "distance_km":
                        best_distance
                    }
                )

        return links