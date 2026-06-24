import { Globe, Search } from "lucide-react";

export default function Navbar() {
    return (
        <div className="relative z-10 w-full">
            <nav
                className="
                    relative
                    flex
                    justify-between
                    items-center
                    px-6
                    py-4
                    bg-[#13151B]
                    border-b
                    border-gray-800
                "
            >
                <div
                    className="
                        text-cyan-400
                        font-bold
                        text-xl
                        flex gap-3 justify-center items-center
                    "
                >
                    <Globe />
                    ORBITALNET
                </div>

                <div
                    className="
                        flex
                        justify-center
                        items-center
                        gap-8
                        text-slate-300
                        text-[18px]
                        tracking-[1px]
                        font-semibold
                    "
                >
                    <span className="hover:text-cyan-400 cursor-pointer transition-colors">Simulation</span>
                    <span className="hover:text-cyan-400 cursor-pointer transition-colors">Telemetry</span>
                    <span className="hover:text-cyan-400 cursor-pointer transition-colors">Network</span>
                    <span className="hover:text-cyan-400 cursor-pointer transition-colors"><Search size={20} /></span>
                </div>
            </nav>
            <div 
                className="
                    absolute 
                    top-full 
                    left-0 
                    w-full 
                    h-12 
                    bg-linear-to-b 
                    from-cyan-500/20 
                    to-transparent 
                    blur-md 
                    pointer-events-none
                " 
            />
        </div>
    );
}