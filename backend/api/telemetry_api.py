from fastapi import APIRouter

from analytics.telemetry_query_service import (
    TelemetryQueryService
)

router = APIRouter()

service = (
    TelemetryQueryService()
)


@router.get("/telemetry/count")

def telemetry_count():

    return {
        "total_events":
        service.total_events()
    }

@router.get("/telemetry/events")

def telemetry_events():

    return service.all_events()

@router.get("/telemetry/latest")

def latest_events():

    return (
        service.latest_events()
    )

@router.get("/telemetry/low-snr")
def low_snr_count():

    return {
        "count":
        service.count_events_by_type(
            "LOW_SNR"
        )
    }

@router.get("/telemetry/link-downs")
def link_down_count():

    return {
        "count":
        service.count_events_by_type(
            "LINK_DOWN"
        )
    }

@router.get("/telemetry/link-recoveries")
def link_recovery_count():

    return {
        "count":
        service.count_events_by_type(
            "LINK_RECOVERED"
        )
    }