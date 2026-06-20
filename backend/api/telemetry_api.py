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