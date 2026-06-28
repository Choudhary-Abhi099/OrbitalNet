from fastapi import FastAPI

from backend.api.network_api import (
    router as network_router
)

from backend.api.telemetry_api import (
    router as telemetry_router
)

from simulation.orbital.tle_loader import (
    TLELoader
)

from simulation.orbital.satellite_factory import (
    SatelliteFactory
)

from simulation.orbital.orbit_propagator import (
    OrbitPropagator
)

from simulation.routing.graph_builder import (
    GraphBuilder
)

from simulation.background_simulation import (
    start_background_simulation
)

from backend.services.network_state_service import (
    network_state_service
)

from backend.websocket.simulation_ws import (
    router as websocket_router
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from backend.api.connectivity_api import (
    router as connectivity_router
)

from backend.api.communication_api import (
    router as communication_router
)

from backend.api.satellite_api import (
    router as satellite_router
)

from backend.api.ground_station_api import (
    router as ground_station_router
)

from backend.api.routes_api import (
    router as routes_router
)
from backend.api.orbit_trails_api import (
    router as orbit_trails_router
)

from backend.api.orbit_paths_api import (
    router as orbit_paths_router
)

from backend.api.visibility_links_api import (
    router as visibility_links_router
)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

@app.on_event("startup")
def startup():
    start_background_simulation()
    print(
        "\n[STARTUP] Initializing network..."
    )

    loader = TLELoader()

    records = loader.load_tle_file(
        "simulation/data/satellites.tle"
    )

    factory = SatelliteFactory()

    satellites = (
        factory.create_satellites(
            records
        )
    )

    propagator = OrbitPropagator()

    for satellite in satellites:

        propagator.update_position(
            satellite
        )

    graph_builder = GraphBuilder()

    graph = (
        graph_builder.build_graph(
            satellites
        )
    )

    network_state_service.update_graph(
        graph
    )

    print(
        f"[STARTUP] Graph initialized "
        f"Nodes={graph.number_of_nodes()} "
        f"Links={graph.number_of_edges()}"
    )


app.include_router(
    telemetry_router
)

app.include_router(
    network_router
)
app.include_router(
    websocket_router
)

app.include_router(
    connectivity_router
)

app.include_router(
    communication_router
)

app.include_router(
    satellite_router
)

app.include_router(
    ground_station_router
)

app.include_router(
    routes_router
)
app.include_router(
    orbit_trails_router
)

app.include_router(
    orbit_paths_router
)

app.include_router(
    visibility_links_router
)