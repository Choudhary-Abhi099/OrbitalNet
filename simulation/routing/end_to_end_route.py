class EndToEndRouter:

    def build_route(
        self,
        user,
        satellite_result,
        ground_station_result
    ):

        return {
            "user": user.user_id,
            "satellite": (
                satellite_result[
                    "satellite"
                ].satellite_id
            ),
            "ground_station": (
                ground_station_result[
                    "station"
                ].station_id
            )
        }