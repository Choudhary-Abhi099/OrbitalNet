# orbit_propagator.py

class OrbitPropagator:

    def propagate(self, satellite, delta_time):

        satellite.longitude += (
            satellite.velocity * delta_time
        )

        if satellite.longitude > 180:
            satellite.longitude -= 360

        satellite.timestamp += delta_time

def get_all_satellites(self):
    return self.satellites.values() 