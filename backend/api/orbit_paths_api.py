from fastapi import APIRouter

from backend.services.orbit_path_state_service import (
    orbit_path_service
)

router = APIRouter()


@router.get("/orbit-paths")
def get_orbit_paths():

    return (
        orbit_path_service
        .get_all_paths()
    )