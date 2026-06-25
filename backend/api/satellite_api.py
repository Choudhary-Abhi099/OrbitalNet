from fastapi import APIRouter

from backend.services.satellite_service import (
    satellite_service
)

from simulation.orbital.constellation_manager import (
    constellation_manager
)
from backend.services.constellation_state_service import (
    constellation_state_service
)

router = APIRouter()


@router.get("/satellites")
def satellites():

    constellation = (
        constellation_state_service
        .get_constellation()
    )

    if constellation is None:

        return []

    satellites = (
        constellation
        .get_all_satellites()
    )

    return (
        satellite_service
        .build_satellite_response(
            satellites
        )
    )