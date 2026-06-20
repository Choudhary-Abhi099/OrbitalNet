from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2


class DistanceCalculator:

    EARTH_RADIUS_KM = 6371

    def calculate_distance(self, sat1, sat2):

        lat1 = radians(sat1.latitude)
        lon1 = radians(sat1.longitude)

        lat2 = radians(sat2.latitude)
        lon2 = radians(sat2.longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            sin(dlat / 2) ** 2
            + cos(lat1)
            * cos(lat2)
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a)
        )

        return self.EARTH_RADIUS_KM * c