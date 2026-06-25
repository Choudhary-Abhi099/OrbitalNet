class SatelliteService:

    def build_satellite_response(
        self,
        satellites
    ):

        return [

            {
                "satellite_id":
                satellite.satellite_id,

                "latitude":
                satellite.latitude,

                "longitude":
                satellite.longitude,

                "altitude_km":
                satellite.altitude_km,

                "status":
                satellite.status
            }

            for satellite in satellites
        ]


satellite_service = (
    SatelliteService()
)