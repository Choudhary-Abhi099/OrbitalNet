class UserConnectivityService:

    def build_connectivity(
        self,
        user,
        satellite,
        ground_station
    ):

        return {
            "user_id":
            user.user_id,

            "connected_satellite":
            satellite.satellite_id,

            "ground_station":
            ground_station.station_id,

            "status":
            "CONNECTED"
        }