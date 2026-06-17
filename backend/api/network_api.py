from fastapi import APIRouter

from analytics.network_statistics_service import (
    NetworkStatisticsService
)

from backend.services.network_state_service import (
    NetworkStateService
)

router = APIRouter()

stats_service = (
    NetworkStatisticsService()
)

state_service = (
    NetworkStateService()
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