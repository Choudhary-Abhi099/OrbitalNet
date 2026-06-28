from fastapi import APIRouter

from backend.services.orbit_trail_state_service import (
    orbit_trail_service
)

router = APIRouter()


@router.get("/orbit-trails")
def get_orbit_trails():

    return (
        orbit_trail_service
        .get_all_trails()
    )