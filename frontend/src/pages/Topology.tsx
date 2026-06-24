import NetworkTopology
from "../components/topology/NetworkTopology";

export default function Topology() {

    return (

        <div
            className="
                min-h-screen
                bg-slate-950
                p-6
            "
        >

            <h1
                className="
                    text-white
                    text-4xl
                    font-bold
                    mb-6
                "
            >
                OrbitalNet Topology
            </h1>

            <NetworkTopology />

        </div>
    );
}