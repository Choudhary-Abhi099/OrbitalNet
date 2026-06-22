from analytics.telemetry_query_service import (
    TelemetryQueryService
)

from analytics.network_statistics_service import (
    NetworkStatisticsService
)

class NetworkHealthService:

    def __init__(self):

        self.telemetry = (
            TelemetryQueryService()
        )

        self.network_stats = (
            NetworkStatisticsService()
        )

    def build_health_report(
        self,
        graph
    ):

        stats = (
            self.network_stats
            .build_statistics(
                graph
            )
        )

        return {

            "satellites":
            stats["satellites"],

            "links":
            stats["links"],

            "average_degree":
            stats["average_degree"],

            "total_events":
            self.telemetry
            .total_events(),

            "low_snr_events":
            self.telemetry
            .count_events_by_type(
                "LOW_SNR"
            ),

            "link_down_events":
            self.telemetry
            .count_events_by_type(
                "LINK_DOWN"
            ),

            "link_recovered_events":
            self.telemetry
            .count_events_by_type(
                "LINK_RECOVERED"
            )
        }