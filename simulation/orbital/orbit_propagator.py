from skyfield.api import EarthSatellite
from skyfield.api import load

class OrbitPropagator:
    def __init__(self):
        self.ts = load.timescale()

    def get_position(self, tle_record):

        satellite = EarthSatellite(
            tle_record["line1"],
            tle_record["line2"],
            tle_record["name"],
            self.ts
        )

        t = self.ts.now()

        geocentric = satellite.at(t)

        subpoint = geocentric.subpoint()

        return {
            "name": tle_record["name"],
            "latitude": float(subpoint.latitude.degrees),
            "longitude": float(subpoint.longitude.degrees),
            "altitude_km": float(subpoint.elevation.km)
        }