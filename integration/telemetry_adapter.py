from datetime import datetime

from database.telemetry_repository import (
    TelemetryRepository
)


class TelemetryAdapter:

    def __init__(self):

        self.repository = (
            TelemetryRepository()
        )

        self.repository.initialize()

    def record_event(
        self,
        event_type,
        data
    ):

        if event_type == "SATELLITE_FAILED":

            satellite = data["satellite"]

            description = (
            f"Satellite Failed: "
            f"{satellite.satellite_id}"
        )

        else:
            description = str(data)

        timestamp = (
            datetime.utcnow()
            .isoformat()
        )

        self.repository.save_event(
            event_type,
            timestamp,
            description
        )

        print(
            f"[TELEMETRY] "
            f"{event_type} saved"
        )