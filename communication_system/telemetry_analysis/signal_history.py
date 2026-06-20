from datetime import datetime


class SignalHistory:

    def __init__(self):

        self.history = []

    def add_record(
        self,
        rssi,
        snr,
        ber
    ):

        self.history.append(
            {
                "timestamp":
                datetime.now(),

                "rssi":
                rssi,

                "snr":
                snr,

                "ber":
                ber
            }
        )

    def get_history(self):

        return self.history
    
    def latest_record(self):

        if not self.history:
            return None

        return self.history[-1]
    

    def record_count(self):
        return len(self.history)