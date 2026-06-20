from simulation.users.user_terminal import UserTerminal


class UserGenerator:

    def generate_users(self):

        return [

            UserTerminal(
                user_id="USER-001",
                latitude=28.6139,
                longitude=77.2090
            ),

            UserTerminal(
                user_id="USER-002",
                latitude=19.0760,
                longitude=72.8777
            ),

            UserTerminal(
                user_id="USER-003",
                latitude=51.5074,
                longitude=-0.1278
            ),

            UserTerminal(
                user_id="USER-004",
                latitude=35.6762,
                longitude=139.6503
            ),

            UserTerminal(
                user_id="USER-005",
                latitude=40.7128,
                longitude=-74.0060
            )
        ]