class UserConnectionManager:

    def __init__(self):

        self.connections = {}

    def connect_user(
        self,
        user_id,
        satellite_id
    ):

        self.connections[user_id] = satellite_id

    def get_connected_satellite(
        self,
        user_id
    ):

        return self.connections.get(user_id)

    def perform_handover(
        self,
        user_id,
        new_satellite_id
    ):

        self.connections[user_id] = (
            new_satellite_id
        )

    def get_all_connections(self):

        return self.connections