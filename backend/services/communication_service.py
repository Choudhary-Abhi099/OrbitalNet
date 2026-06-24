class CommunicationService:

    def __init__(self):

        self.latest_report = {

        "Distance (km)": 650,

        "FSPL (dB)": 170.3,

        "Received Power (dBm)": -79,

        "RSSI (dBm)": -79,

        "SNR (dB)": 21,

        "BER": 1e-08,

        "Latency (ms)": 2.1,

        "Packet Loss (%)": 0.1,

        "Status": "ONLINE"
    }

    def update_report(
        self,
        report
    ):

        self.latest_report = report

    def get_report(self):

        return self.latest_report


communication_service = (
    CommunicationService()
)