from skyfield.api import EarthSatellite
from skyfield.api import load
from datetime import timedelta


class OrbitPropagator:

    def __init__(self):
        self.ts = load.timescale()

    def update_position(self, satellite):

        skyfield_sat = EarthSatellite(
            satellite.tle_line1,
            satellite.tle_line2,
            satellite.satellite_id,
            self.ts
        )

        t = self.ts.now()

        geocentric = skyfield_sat.at(t)

        subpoint = geocentric.subpoint()

        satellite.latitude = float(
            subpoint.latitude.degrees
        )

        satellite.longitude = float(
            subpoint.longitude.degrees
        )

        satellite.altitude_km = float(
            subpoint.elevation.km
        )

    def get_position_at(
        self,
        satellite,
        dt
    ):

        skyfield_sat = EarthSatellite(
            satellite.tle_line1,
            satellite.tle_line2,
            satellite.satellite_id,
            self.ts
        )

        t = self.ts.from_datetime(dt)

        geocentric = skyfield_sat.at(t)

        subpoint = geocentric.subpoint()

        return {
            "latitude":
            float(
                subpoint.latitude.degrees
            ),

            "longitude":
            float(
                subpoint.longitude.degrees
            ),

            "altitude_km":
            float(
                subpoint.elevation.km
            )
        }