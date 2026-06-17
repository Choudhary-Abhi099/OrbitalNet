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