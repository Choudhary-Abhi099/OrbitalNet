export interface CommunicationReport {

    ["Distance (km)"]: number;

    ["FSPL (dB)"]: number;

    ["Received Power (dBm)"]: number;

    ["RSSI (dBm)"]: number;

    ["SNR (dB)"]: number;

    BER: number;

    ["Latency (ms)"]: number;

    ["Packet Loss (%)"]: number;

    Status: string;
}