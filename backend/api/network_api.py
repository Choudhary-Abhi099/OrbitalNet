from fastapi import APIRouter

from analytics.network_statistics_service import (
    NetworkStatisticsService
)

from backend.services.network_state_service import (
    network_state_service
)

from analytics.network_health_service import (
    NetworkHealthService
)
router = APIRouter()

stats_service = (
    NetworkStatisticsService()
)

health_service = (
    NetworkHealthService()
)

@router.get("/network/statistics")
def network_statistics():

    graph = (
        network_state_service.get_graph()
    )
    print(
        network_state_service.get_graph()
    )
    if graph is None:

        return {
            "message":
            "Network graph not initialized"
        }

    return (
        stats_service.build_statistics(
            graph
        )
    )

@router.get("/network/health")
def network_health():

    graph = (
        network_state_service.get_graph()
    )

    if graph is None:
        return{
            "message":
            "Network graph is not initalized"
        }

    return (
        health_service
        .build_health_report(
            graph
        )
    )