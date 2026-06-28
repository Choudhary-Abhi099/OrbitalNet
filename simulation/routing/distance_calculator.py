from math import radians
from math import sin
from math import cos
from math import sqrt


class DistanceCalculator:

    EARTH_RADIUS_KM = 6371

    def calculate_distance(
        self,
        node1,
        node2
    ):

        altitude1 = getattr(
            node1,
            "altitude_km",
            0
        )

        altitude2 = getattr(
            node2,
            "altitude_km",
            0
        )

        r1 = (
            self.EARTH_RADIUS_KM
            + altitude1
        )

        r2 = (
            self.EARTH_RADIUS_KM
            + altitude2
        )

        lat1 = radians(node1.latitude)
        lon1 = radians(node1.longitude)

        lat2 = radians(node2.latitude)
        lon2 = radians(node2.longitude)

        x1 = (
            r1
            * cos(lat1)
            * cos(lon1)
        )

        y1 = (
            r1
            * cos(lat1)
            * sin(lon1)
        )

        z1 = (
            r1
            * sin(lat1)
        )

        x2 = (
            r2
            * cos(lat2)
            * cos(lon2)
        )

        y2 = (
            r2
            * cos(lat2)
            * sin(lon2)
        )

        z2 = (
            r2
            * sin(lat2)
        )

        return sqrt(
            (x2 - x1) ** 2
            + (y2 - y1) ** 2
            + (z2 - z1) ** 2
        )