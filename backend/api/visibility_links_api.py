from fastapi import APIRouter

from backend.services.visibility_link_state_service import (
    visibility_link_state_service
)

router = APIRouter()


@router.get(
    "/visibility-links"
)
def visibility_links():

    return (
        visibility_link_state_service
        .get_links()
    )