import StatCard from "./StatCard";

import type {
    NetworkStats
} from "../../types/network";

interface Props {

    stats: NetworkStats;
}

export default function NetworkStats({
    stats
}: Props) {

    return (

        <div
            className="
                grid
                grid-cols-3
                gap-6
            "
        >

            <StatCard
                title="Satellites"
                value={stats.satellites}
            />

            <StatCard
                title="Links"
                value={stats.links}
            />

            <StatCard
                title="Average Degree"
                value={
                    stats.average_degree
                }
            />

        </div>
    );
}