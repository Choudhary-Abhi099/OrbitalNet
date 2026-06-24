interface Props {

    satellites: number;

    links: number;

    averageDegree: number;
}

export default function NetworkOverview(
    {
        satellites,
        links,
        averageDegree
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
                    mb-6
                "
            >
                Network Overview
            </h2>

            <div className="space-y-4">

                <div className="flex justify-between">
                    <span>Satellites</span>
                    <span>{satellites}</span>
                </div>

                <div className="flex justify-between">
                    <span>Links</span>
                    <span>{links}</span>
                </div>

                <div className="flex justify-between">
                    <span>Avg Degree</span>
                    <span>{averageDegree}</span>
                </div>

                <div className="flex justify-between">
                    <span>Health</span>

                    <span
                        className="
                            text-green-400
                        "
                    >
                        HEALTHY
                    </span>
                </div>

            </div>

        </div>
    );
}