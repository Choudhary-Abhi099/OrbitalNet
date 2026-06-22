from analytics.telemetry_query_service import (
    TelemetryQueryService
)

from analytics.network_statistics_service import (
    NetworkStatisticsService
)


class NetworkHealthService:

    def __init__(
        self,
        constellation_manager,
        graph
    ):

        self.telemetry = (
            TelemetryQueryService()
        )

        self.statistics = (
            NetworkStatisticsService(
                constellation_manager,
                graph
            )
        )

    def get_health_report(self):

        low_snr = (
            self.telemetry
            .count_events_by_type(
                "LOW_SNR"
            )
        )

        link_down = (
            self.telemetry
            .count_events_by_type(
                "LINK_DOWN"
            )
        )

        link_recovered = (
            self.telemetry
            .count_events_by_type(
                "LINK_RECOVERED"
            )
        )

        stats = (
            self.statistics
            .get_statistics()
        )

        return {

            "satellites":
            stats["satellites"],

            "links":
            stats["links"],

            "average_degree":
            stats["average_degree"],

            "low_snr_events":
            low_snr,

            "link_down_events":
            link_down,

            "link_recovered_events":
            link_recovered
        }