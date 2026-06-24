from fastapi import APIRouter

from backend.services.communication_service import (
    communication_service
)

router = APIRouter()


@router.get(
    "/communication/report"
)
def communication_report():

    return (
        communication_service
        .get_report()
    )