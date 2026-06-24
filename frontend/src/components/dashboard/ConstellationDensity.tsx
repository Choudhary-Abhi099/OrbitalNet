import { Orbit } from "lucide-react"; // Fits perfectly for a constellation symbol

interface ConstellationProps {
    activeSatellites: number;
    failedSatellites?: number;
    groundStations?: number;
    connectedUsers?: string;
}

export default function ConstellationDensity({
    activeSatellites,
    failedSatellites = 0,
    groundStations = 24,
    connectedUsers = "8.4k"
}: ConstellationProps) {
    const radius = 50;
    const strokeWidth = 4;
    const circumference = 2 * Math.PI * radius;
    const fillPercentage = 75; 
    const strokeDashoffset = circumference - (fillPercentage / 100) * circumference;

    return (
        <div
            className="
                bg-[#0B0F17]
                p-8
                border
                border-slate-900/80
                font-mono
                tracking-wider
                w-full
            "
        >
            <div className="flex items-center gap-3 mb-8">
                <Orbit className="text-cyan-400 w-6 h-6 animate-[spin_20s_linear_infinite]" strokeWidth={2} />
                <h2 className="text-slate-300 font-bold text-base tracking-widest">
                    CONSTELLATION DENSITY
                </h2>
            </div>
            <div className="flex justify-center items-center relative my-10">
                <svg 
                    className="w-44 h-44 transform -rotate-90 drop-shadow-[0_0_12px_rgba(34,211,238,0.3)]"
                    viewBox="0 0 120 120"
                >
                    <circle
                        cx="60"
                        cy="60"
                        r={radius}
                        className="stroke-[#131924]"
                        strokeWidth={strokeWidth}
                        fill="transparent"
                    />
                    <circle
                        cx="60"
                        cy="60"
                        r={radius}
                        className="stroke-cyan-400 transition-all duration-500 ease-out"
                        strokeWidth={strokeWidth}
                        strokeDasharray={circumference}
                        strokeDashoffset={strokeDashoffset}
                        strokeLinecap="round"
                        fill="transparent"
                    />
                </svg>

                <div className="absolute text-center flex flex-col justify-center items-center">
                    <span className="text-2xl font-bold text-slate-100 tracking-normal">
                        {activeSatellites.toLocaleString()}
                    </span>
                    <span className="text-[10px] text-slate-500 font-bold mt-1 tracking-widest uppercase">
                        Active Satellites
                    </span>
                </div>
            </div>
            <div className="space-y-0 text-sm mt-6">
                <div className="flex justify-between items-center py-3 border-b border-slate-900/50">
                    <span className="text-slate-400 font-medium">FAILED SATELLITES</span>
                    <span className="text-[#FFA39E] font-bold text-base shadow-[0_0_8px_rgba(255,163,158,0.1)]">
                        {failedSatellites}
                    </span>
                </div>

                <div className="flex justify-between items-center py-3 border-b border-slate-900/50">
                    <span className="text-slate-400 font-medium">GROUND STATIONS</span>
                    <span className="text-slate-200 font-bold text-base">
                        {groundStations}
                    </span>
                </div>
                <div className="flex justify-between items-center py-3">
                    <span className="text-slate-400 font-medium">CONNECTED USERS</span>
                    <span className="text-cyan-400 font-bold text-base lowercase">
                        {connectedUsers}
                    </span>
                </div>

            </div>
        </div>
    );
}