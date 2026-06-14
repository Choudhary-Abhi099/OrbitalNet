from simulation.ground.ground_station import (
    GroundStation
)


class GroundStationGenerator:

    def generate_stations(self):

        return [

            GroundStation(
                station_id="GS-DELHI",
                latitude=28.6139,
                longitude=77.2090
            ),

            GroundStation(
                station_id="GS-LONDON",
                latitude=51.5074,
                longitude=-0.1278
            ),

            GroundStation(
                station_id="GS-TOKYO",
                latitude=35.6762,
                longitude=139.6503
            ),

            GroundStation(
                station_id="GS-NEWYORK",
                latitude=40.7128,
                longitude=-74.0060
            )
        ]