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
                station_id="GS-MUMBAI",
                latitude=19.0760,
                longitude=72.8777
            ),
            GroundStation(
                station_id="GS-TOKYO",
                latitude=35.6762,
                longitude=139.6503
            ),

            GroundStation(
                station_id="GS-SEOUL",
                latitude=37.5665,
                longitude=126.9780
            ),

            GroundStation(
                station_id="GS-SINGAPORE",
                latitude=1.3521,
                longitude=103.8198
            ),

            GroundStation(
                station_id="GS-SYDNEY",
                latitude=-33.8688,
                longitude=151.2093
            ),

            GroundStation(
                station_id="GS-LONDON",
                latitude=51.5074,
                longitude=-0.1278
            ),

            GroundStation(
                station_id="GS-PARIS",
                latitude=48.8566,
                longitude=2.3522
            ),

            GroundStation(
                station_id="GS-BERLIN",
                latitude=52.5200,
                longitude=13.4050
            ),

            GroundStation(
                station_id="GS-STOCKHOLM",
                latitude=59.3293,
                longitude=18.0686
            ),

            GroundStation(
                station_id="GS-NEWYORK",
                latitude=40.7128,
                longitude=-74.0060
            ),

            GroundStation(
                station_id="GS-CHICAGO",
                latitude=41.8781,
                longitude=-87.6298
            ),

            GroundStation(
                station_id="GS-LOSANGELES",
                latitude=34.0522,
                longitude=-118.2437
            ),

            GroundStation(
                station_id="GS-TORONTO",
                latitude=43.6532,
                longitude=-79.3832
            ),

            GroundStation(
                station_id="GS-SAOPAULO",
                latitude=-23.5505,
                longitude=-46.6333
            ),

            GroundStation(
                station_id="GS-CAIRO",
                latitude=30.0444,
                longitude=31.2357
            ),

            GroundStation(
                station_id="GS-CAPETOWN",
                latitude=-33.9249,
                longitude=18.4241
            ),

            GroundStation(
                station_id="GS-DUBAI",
                latitude=25.2048,
                longitude=55.2708
            )
        ]