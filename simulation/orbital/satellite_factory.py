from simulation.orbital.satellite import Satellite


class SatelliteFactory:

    def create_satellite(self, tle_record):

        return Satellite(
            satellite_id=tle_record["name"],
            latitude=0.0,
            longitude=0.0,
            altitude_km=0.0,
            status="ACTIVE",
            tle_line1=tle_record["line1"],
            tle_line2=tle_record["line2"]
        )

    def create_satellites(self, tle_records):

        satellites = []

        for record in tle_records:
            satellites.append(
                self.create_satellite(record)
            )

        return satellites