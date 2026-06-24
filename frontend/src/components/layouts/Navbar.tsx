export default function Navbar() {

    return (

        <nav
            className="
                flex
                justify-between
                items-center
                px-8
                py-4
                border-b
                border-cyan-900
                bg-slate-950
            "
        >

            <div
                className="
                    text-cyan-400
                    font-bold
                    text-xl
                "
            >
                ORBITALNET
            </div>

            <div
                className="
                    flex
                    gap-8
                    text-slate-300
                "
            >
                <span>Simulation</span>
                <span>Telemetry</span>
                <span>Network</span>
            </div>

        </nav>
    );
}