import {
    Globe,
    Satellite,
    BarChart3,
    Bell
} from "lucide-react";

export default function BottomNavigation() {
    return (
        <div
            className="
                w-full
                bg-[#0B0F17]
                py-4
                px-8
                flex
                justify-around
                items-center
                font-mono
                tracking-wider
                select-none
            "
        >
            <div
                className="
                    flex
                    flex-col
                    items-center
                    cursor-pointer
                    text-cyan-400
                    drop-shadow-[0_0_10px_rgba(34,211,238,0.45)]
                "
            >
                <Globe size={22} strokeWidth={2} />
                <span className="text-[11px] font-semibold mt-2">
                    Globe
                </span>
            </div>
            <div
                className="
                    flex
                    flex-col
                    items-center
                    cursor-pointer
                    text-[#8A99AD]
                    hover:text-slate-200
                    transition-colors
                "
            >
                <Satellite size={22} strokeWidth={1.8} />
                <span className="text-[11px] mt-2">
                    Constellation
                </span>
            </div>
            <div
                className="
                    flex
                    flex-col
                    items-center
                    cursor-pointer
                    text-[#8A99AD]
                    hover:text-slate-200
                    transition-colors
                "
            >
                <BarChart3 size={22} strokeWidth={1.8} />
                <span className="text-[11px] mt-2">
                    Network
                </span>
            </div>

            <div
                className="
                    relative
                    flex
                    flex-col
                    items-center
                    cursor-pointer
                    text-[#8A99AD]
                    hover:text-slate-200
                    transition-colors
                "
            >
                <span className="absolute top-0 right-1 w-1.75 h-1.75 bg-[#FFA39E] rounded-full shadow-[0_0_6px_#FFA39E]" />
                <Bell size={22} strokeWidth={1.8} />
                <span className="text-[11px] mt-2">
                    Alerts
                </span>
            </div>

        </div>
    );
}