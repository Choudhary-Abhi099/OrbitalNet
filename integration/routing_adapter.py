class RoutingAdapter:

    def satellite_failed(
        self,
        data
    ):

        satellite = data[
            "satellite"
        ]

        print(
            f"[ROUTING] "
            f"Recalculating routes "
            f"after failure of "
            f"{satellite.satellite_id}"
        )