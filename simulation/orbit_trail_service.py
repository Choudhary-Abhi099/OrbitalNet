from collections import defaultdict


class OrbitTrailService:

    def __init__(self):
        self.trails = defaultdict(list)
        self.max_points = 50

    def add_position(self, satellite):

        self.trails[
            satellite.satellite_id
        ].append(
            {
                "latitude": satellite.latitude,
                "longitude": satellite.longitude,
                "altitude_km": satellite.altitude_km
            }
        )

        if len(
            self.trails[
                satellite.satellite_id
            ]
        ) > self.max_points:

            self.trails[
                satellite.satellite_id
            ].pop(0)

    def get_all_trails(self):
        return self.trails