from database.telemetry_repository import(TelemetryRepository)
class TelemetryQueryService:

    def __init__(self):

        self.repository = (
            TelemetryRepository()
        )

    def total_events(self):

        return (
            self.repository
            .count_events()
        )

    def all_events(self):

        return (
            self.repository
            .get_all_events()
        )
    def latest_events(
        self,
        limit=10
    ):

        return (
            self.repository
            .latest_events(limit)
        )
    
    def count_events_by_type(
        self,
        event_type
    ):

        return (
            self.repository
            .count_events_by_type(
                event_type
            )
        )