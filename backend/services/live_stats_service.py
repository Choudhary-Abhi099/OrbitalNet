class LiveStatsService:

    def __init__(self):

        self.stats = {}

    def update(
        self,
        stats
    ):

        self.stats = stats

    def get_stats(self):

        return self.stats


live_stats_service = (
    LiveStatsService()
)