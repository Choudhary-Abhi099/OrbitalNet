from fastapi import FastAPI
from backend.api.network_api import (
    router as network_router
)
from backend.api.telemetry_api import (
    router as telemetry_router
)

app = FastAPI()

app.include_router(
    telemetry_router
)
app.include_router(
    network_router
)