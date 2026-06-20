from skyfield.api import EarthSatellite
from skyfield.api import load


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