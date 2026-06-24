import { Network } from "lucide-react";

interface Props {
    satellites: number;
    links: number;
    averageDegree: number;
}

export default function NetworkOverview({
    satellites,
    links,
    averageDegree
}: Props) {
    return (
        <div
            className="
                bg-[#0B0F17]
                p-8
                border
                border-slate-900/80
                font-mono
                tracking-wider
                max-w-md
                w-full
            "
        >
            <div className="flex items-center gap-3 mb-8">
                <Network className="text-cyan-400 w-6 h-6" strokeWidth={2.5} />
                <h2 className="text-slate-300 font-bold text-base tracking-widest">
                    NETWORK OVERVIEW
                </h2>
            </div>

            <div className="space-y-0 text-sm">
                <div className="flex justify-between items-center py-3 border-b border-slate-900/50">
                    <span className="text-slate-400 font-medium">Satellites</span>
                    <span className="text-cyan-400 font-bold text-base">{satellites}</span>
                </div>

                <div className="flex justify-between items-center py-3 border-b border-slate-900/50">
                    <span className="text-slate-400 font-medium">Links</span>
                    <span className="text-cyan-400 font-bold text-base">{links}</span>
                </div>
                <div className="flex justify-between items-center py-3 border-b border-slate-900/50">
                    <span className="text-slate-400 font-medium">Avg Degree</span>
                    <span className="text-cyan-400 font-bold text-base">
                        {averageDegree.toFixed(2)}
                    </span>
                </div>
                <div className="flex justify-between items-center py-3">
                    <span className="text-slate-400 font-medium">Health</span>
                    <span className="text-emerald-400 font-bold text-base tracking-wide">
                        Healthy
                    </span>
                </div>

            </div>
        </div>
    );
}