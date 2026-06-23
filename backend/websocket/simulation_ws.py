import asyncio

from backend.services.live_stats_service import (
    live_stats_service
)

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from backend.websocket.connection_manager import (
    manager
)

router = APIRouter()

@router.websocket("/ws/simulation")
async def simulation_socket(
    websocket: WebSocket
):

    await manager.connect(
        websocket
    )

    try:

        while True:

            stats = (
                live_stats_service
                .get_stats()
            )

            await websocket.send_json(
                stats
            )

            await asyncio.sleep(
                5
            )

    except WebSocketDisconnect:

        manager.disconnect(
            websocket
        )