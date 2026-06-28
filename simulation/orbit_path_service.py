from datetime import datetime
from datetime import timedelta
from skyfield.api import utc


class OrbitPathService:

    def __init__(self):
        self.paths = {}

    def generate_path(
        self,
        satellite,
        propagator
    ):

        points = []

        start = datetime.now(
            tz=utc
        )

        for minute in range(0, 100):

            future_time = (
                start +
                timedelta(
                    minutes=minute
                )
            )

            point = (
                propagator
                .get_position_at(
                    satellite,
                    future_time
                )
            )

            points.append(
                point
            )

        self.paths[
            satellite.satellite_id
        ] = points

    def get_all_paths(
        self
    ):
        return self.paths