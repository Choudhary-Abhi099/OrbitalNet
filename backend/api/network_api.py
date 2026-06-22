from fastapi import APIRouter

from analytics.network_statistics_service import (
    NetworkStatisticsService
)

from backend.services.network_state_service import (
    NetworkStateService
)

from analytics.network_health_service import (
    NetworkHealthService
)
router = APIRouter()

stats_service = (
    NetworkStatisticsService()
)

state_service = (
    NetworkStateService()
)

health_service = (
    NetworkHealthService()
)

@router.get("/network/statistics")
def network_statistics():

    graph = (
        state_service.get_graph()
    )

    return (
        stats_service.build_statistics(
            graph
        )
    )

@router.get("/network/health")
def network_health():

    graph = (
        state_service.get_graph()
    )

    return (
        health_service
        .build_health_report(
            graph
        )
    )