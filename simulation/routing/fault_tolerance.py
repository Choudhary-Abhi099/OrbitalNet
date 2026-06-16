class FaultToleranceManager:

    def fail_satellite(
        self,
        satellite
    ):

        satellite.status = "FAILED"

    def recover_satellite(
        self,
        satellite
    ):

        satellite.status = "ACTIVE"

    def get_active_satellites(
        self,
        satellites
    ):

        return [
            satellite
            for satellite in satellites
            if satellite.status == "ACTIVE"
        ]