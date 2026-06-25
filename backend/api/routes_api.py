from fastapi import APIRouter

from backend.services.route_state_service import (
    route_state_service
)

router = APIRouter()

@router.get("/routes")
def routes():

    return (
        route_state_service
        .get_routes()
    )