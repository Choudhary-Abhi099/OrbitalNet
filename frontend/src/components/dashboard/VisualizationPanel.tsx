interface Props {

    satellites?: number;

    links?: number;
}
import TopologyGraph from "./TopologyGraph";
export default function VisualizationPanel(
    {
        satellites = 167,
        links = 427
    }: Props
) {

    return (

        <div
            className="
                bg-slate-800
                border
                border-cyan-900
                rounded-xl
                p-6
                min-h-162.5
                shadow-[0_0_15px_rgba(34,211,238,0.10)]
            "
        >

            <div
                className="
                    flex
                    justify-between
                    items-center
                    mb-6
                "
            >

                <h2
                    className="
                        text-cyan-300
                        uppercase
                        tracking-widest
                        text-sm
                        font-semibold
                    "
                >
                    Visualizer V2.4
                </h2>

                <div
                    className="
                        text-green-400
                        text-xs
                        font-semibold
                    "
                >
                    ● LIVE
                </div>

            </div>

            <div
                className="
                    flex
                    gap-3
                    mb-6
                "
            >

                <div
                    className="
                        px-3
                        py-1
                        rounded-full
                        border
                        border-cyan-800
                        text-cyan-300
                        text-xs
                    "
                >
                    SAT {satellites}
                </div>

                <div
                    className="
                        px-3
                        py-1
                        rounded-full
                        border
                        border-cyan-800
                        text-cyan-300
                        text-xs
                    "
                >
                    LINKS {links}
                </div>

                <div
                    className="
                        px-3
                        py-1
                        rounded-full
                        border
                        border-green-700
                        text-green-400
                        text-xs
                    "
                >
                    HEALTHY
                </div>

            </div>

            <div
                className="
                    h-130
                    rounded-xl
                    border
                    border-slate-700
                    flex
                    items-center
                    justify-center
                    relative
                    overflow-hidden
                "
            >
                <TopologyGraph />

            </div>

        </div>
    );
}