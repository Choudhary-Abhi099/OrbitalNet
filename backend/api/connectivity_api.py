from fastapi import APIRouter

router = APIRouter()

@router.get("/user/connectivity")
def user_connectivity():

    return {
        "user_id": "user-1",
        "connected_satellite": "SCD 1",
        "ground_station": "GS-DELHI",
        "status": "CONNECTED"
    }