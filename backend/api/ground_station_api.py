from fastapi import APIRouter

from simulation.ground.ground_station_generator import (
    GroundStationGenerator
)

router = APIRouter()


@router.get("/ground-stations")
def ground_stations():

    stations = (
        GroundStationGenerator()
        .generate_stations()
    )

    return [

        {
            "station_id":
            station.station_id,

            "latitude":
            station.latitude,

            "longitude":
            station.longitude,

            "status":
            station.status
        }

        for station in stations
    ]