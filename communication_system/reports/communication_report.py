def generate_communication_report(
    distance,
    fspl,
    received_power,
    rssi,
    snr,
    ber,
    latency,
    packet_loss,
    status
):

    report = {
        "Distance (km)": round(distance, 2),
        "FSPL (dB)": round(fspl, 2),
        "Received Power (dBm)": round(received_power, 2),
        "RSSI (dBm)": round(rssi, 2),
        "SNR (dB)": round(snr, 2),
        "BER": ber,
        "Latency (ms)": round(latency, 2),
        "Packet Loss (%)": packet_loss,
        "Status": status
    }

    return report