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