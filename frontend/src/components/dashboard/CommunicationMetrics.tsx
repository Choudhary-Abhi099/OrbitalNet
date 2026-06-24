// import type {
//     CommunicationReport
// } from "../../types/communication";
interface Props {

    communication: {

        status: string;

        rssi: number;

        snr: number;

        latency: number;

        packet_loss: number;
    };
}

export default function CommunicationMetrics(
    {
        communication
    }: Props
) {

    return (

        <div
            className="
                 bg-slate-800
    rounded-xl
    p-6
    border
    border-cyan-900
            "
        >

            <h2
                className="
                    text-xl
                    font-bold
                    mb-4
                "
            >
                Communication Metrics
            </h2>

            <div className="space-y-2">

                <p>
                    <strong>Status:</strong>
                    {" "}
                    {communication.status}
                </p>

                <p>
                    <strong>RSSI:</strong>
                    {" "}
                    {communication.rssi} dBm
                </p>

                <p>
                    <strong>SNR:</strong>
                    {" "}
                    {communication.snr} dB
                </p>

                <p>
                    <strong>Latency:</strong>
                    {" "}
                    {communication.latency} ms
                </p>

                <p>
                    <strong>Packet Loss:</strong>
                    {" "}
                    {communication.packet_loss} %
                </p>

            </div>

        </div>
    );
}