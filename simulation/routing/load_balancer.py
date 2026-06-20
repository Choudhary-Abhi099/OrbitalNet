class LoadBalancer:

    def find_most_loaded_satellite(
        self,
        usage_stats
    ):

        if not usage_stats:
            return None

        return max(
            usage_stats,
            key=usage_stats.get
        )

    def find_least_loaded_satellite(
        self,
        usage_stats
    ):

        if not usage_stats:
            return None

        return min(
            usage_stats,
            key=usage_stats.get
        )