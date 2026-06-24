import { useState } from "react";
import { Wrench, ChevronDown, ChevronUp } from "lucide-react";
import EventLog from "./EventLog";

export default function AdvancedTools() {
    const [expanded, setExpanded] = useState(false);

    return (
        <div
            className="
                bg-[#0B0F17]
                border
                border-slate-900/80
                p-8
                font-mono
                tracking-wider
                w-full
            "
        >
            {/* Header with Tools Icon */}
            <div className="flex items-center gap-3 mb-6">
                <Wrench className="text-slate-400 w-5 h-5" strokeWidth={2.5} />
                <h2 className="text-slate-300 font-bold text-base tracking-widest uppercase">
                    ADVANCED TOOLS
                </h2>
            </div>

            <button
                onClick={() => setExpanded(!expanded)}
                className="
                    w-full
                    bg-[#121622]/40
                    border
                    border-slate-900
                    hover:border-slate-800
                    transition-colors
                    p-5
                    flex
                    flex-col
                    justify-center
                    items-center
                    gap-2
                    mb-8
                "
            >
                <span className="text-cyan-400">
                    {expanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                </span>
                <span className="text-slate-200 text-sm font-medium tracking-wide">
                    Show Stress Test Simulator
                </span>
            </button>
            {expanded && (
                <div className="mb-8 space-y-2.5 animate-fadeIn">
                    <button className="w-full p-3.5 bg-red-950/10 hover:bg-red-950/20 border border-red-900/40 text-red-400 text-left text-xs transition-colors font-semibold">
                        &gt; Trigger Signal Jamming
                    </button>
                    <button className="w-full p-3.5 bg-amber-950/10 hover:bg-amber-950/20 border border-amber-900/40 text-amber-400 text-left text-xs transition-colors font-semibold">
                        &gt; Simulate Solar Storm
                    </button>
                    <button className="w-full p-3.5 bg-cyan-950/10 hover:bg-cyan-950/20 border border-cyan-900/40 text-cyan-400 text-left text-xs transition-colors font-semibold">
                        &gt; Random Node Failure
                    </button>
                </div>
            )}
            <div className="border-t border-slate-900/60 my-6 w-full" />
            <EventLog />
        </div>
    );
}