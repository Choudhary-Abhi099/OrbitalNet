import NetworkStats
from "../components/dashboard/NetworkStats";

import {
    useSimulationSocket
} from "../hooks/useSimulationSocket";

export default function Dashboard() {

    const stats =
        useSimulationSocket();

    if (!stats) {

        return (

            <div
                className="
                    p-10
                    text-white
                "
            >
                Connecting...
            </div>
        );
    }

    return (

        <div
            className="
                min-h-screen
                bg-slate-950
                text-white
                p-10
            "
        >

            <h1
                className="
                    text-4xl
                    font-bold
                    mb-10
                "
            >
                OrbitalNet Dashboard
            </h1>

            <NetworkStats
                stats={stats}
            />

        </div>
    );
}