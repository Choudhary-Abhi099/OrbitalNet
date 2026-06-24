import { useState } from "react";

export default function EnvironmentSettings() {
    const [atmosphereEnabled, setAtmosphereEnabled] = useState(false);
    const [latencyEnabled, setLatencyEnabled] = useState(true);

    return (
        <div
            className="
                bg-[#0B0F17]
                border
                border-slate-900/80
                p-5.5
                font-mono
                tracking-wider
                w-full
            "
        >
            <div className="flex items-center gap-3 mb-4 text-cyan-400">
                <span className="font-bold text-lg select-none">&lt;···&gt;</span>
                <h2 className="text-slate-300 font-bold text-base tracking-widest uppercase">
                    ENVIRONMENT SETTINGS
                </h2>
            </div>
            <div className="flex gap-6">
                <button
                    onClick={() => setAtmosphereEnabled(!atmosphereEnabled)}
                    className={`
                        flex
                        items-center
                        justify-between
                        px-5
                        py-4
                        flex-1
                        border
                        transition-all
                        duration-200
                        ${atmosphereEnabled 
                            ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400 shadow-[0_0_15px_rgba(34,211,238,0.05)]" 
                            : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
                        }
                    `}
                >
                    <span className="text-sm font-medium">Atmo Interf.</span>
                    <div 
                        className={`
                            relative w-9 h-5 rounded-full transition-colors duration-200 p-0.5
                            ${atmosphereEnabled ? "bg-cyan-400" : "bg-slate-800"}
                        `}
                    >
                        <div 
                            className={`
                                w-4 h-4 rounded-full bg-[#0B0F17] shadow-sm transform transition-transform duration-200
                                ${atmosphereEnabled ? "translate-x-4" : "translate-x-0"}
                            `}
                        />
                    </div>
                </button>
                <button
                    onClick={() => setLatencyEnabled(!latencyEnabled)}
                    className={`
                        flex
                        items-center
                        justify-between
                        px-5
                        py-4
                        flex-1
                        border
                        transition-all
                        duration-200
                        ${latencyEnabled 
                            ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400 shadow-[0_0_15px_rgba(34,211,238,0.05)]" 
                            : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
                        }
                    `}
                >
                    <span className="text-sm font-medium">Ground Latency</span>
                    <div 
                        className={`
                            relative w-9 h-5 rounded-full transition-colors duration-200 p-0.5
                            ${latencyEnabled ? "bg-cyan-400" : "bg-slate-800"}
                        `}
                    >
                        <div 
                            className={`
                                w-4 h-4 rounded-full bg-[#0B0F17] shadow-sm transform transition-transform duration-200
                                ${latencyEnabled ? "translate-x-4" : "translate-x-0"}
                            `}
                        />
                    </div>
                </button>

            </div>
        </div>
    );
}