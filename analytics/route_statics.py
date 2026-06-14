class RouteStatistics:

    def satellite_usage(
        self,
        routes
    ):

        usage = {}

        for route in routes:

            satellite = route[
                "satellite"
            ]

            usage[satellite] = (
                usage.get(
                    satellite,
                    0
                ) + 1
            )

        return usage

    def ground_station_usage(
        self,
        routes
    ):

        usage = {}

        for route in routes:

            station = route[
                "ground_station"
            ]

            usage[station] = (
                usage.get(
                    station,
                    0
                ) + 1
            )

        return usage