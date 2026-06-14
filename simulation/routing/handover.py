class HandoverManager:

    def should_handover(
        self,
        current_distance,
        candidate_distance,
        threshold_km=50
    ):

        improvement = (
            current_distance
            - candidate_distance
        )

        return improvement > threshold_km