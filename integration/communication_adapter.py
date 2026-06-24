from integration.events import (
    LOW_SNR,
    LINK_DOWN,
    LINK_RECOVERED
)
from backend.services.communication_service import (
    communication_service
)

class CommunicationAdapter:

    LOW_SNR_THRESHOLD = 10

    def __init__(
        self,
        event_bus
    ):

        self.event_bus = event_bus

        self.link_status_cache = {}

    def process_report(
        self,
        satellite_id,
        report
    ):  
        
        communication_service.update_report(
             report
        )
        snr = report["SNR (dB)"]

        status = report["Status"]

        self._check_low_snr(
            satellite_id,
            snr
        )

        self._check_link_status(
            satellite_id,
            status
        )

    def _check_low_snr(
        self,
        satellite_id,
        snr
    ):

        if snr < self.LOW_SNR_THRESHOLD:

            self.event_bus.publish(
                LOW_SNR,
                {
                    "satellite_id": satellite_id,
                    "snr": snr
                }
            )

    def _check_link_status(
        self,
        satellite_id,
        status
    ):

        previous_status = (
            self.link_status_cache.get(
                satellite_id,
                "ONLINE"
            )
        )

        if status == "OFFLINE":

            self.event_bus.publish(
                LINK_DOWN,
                {
                    "satellite_id": satellite_id
                }
            )

        elif (
            previous_status == "OFFLINE"
            and status == "ONLINE"
        ):

            self.event_bus.publish(
                LINK_RECOVERED,
                {
                    "satellite_id": satellite_id
                }
            )

        self.link_status_cache[
            satellite_id
        ] = status