import { useEffect, useState } from "react";

export default function StatusPanel() {
    const [epochTime, setEpochTime] = useState("");

    useEffect(() => {
        const updateTime = () => {
            const decimalTail = (Math.random() * 900 + 100).toFixed(0);
            const standardTimestamp = Math.floor(Date.now() / 1000);
            setEpochTime(`${standardTimestamp}.${decimalTail}`);
        };

        const interval = setInterval(updateTime, 140);
        return () => clearInterval(interval);
    }, []);

    return (
        <div
            className="
                bg-[#0B0F17]
                border
                border-slate-900/80
                p-5
                font-mono
                tracking-wider
                w-full
            "
        >
            <div
                className="
                    grid
                    grid-cols-[1fr_auto_1fr]
                    items-center
                "
            >
                <div className="pl-2">
                    <p
                        className="
                            text-[11px]
                            text-slate-400
                            font-semibold
                            tracking-widest
                            uppercase
                            mb-1.5
                        "
                    >
                        EPOCH TIME
                    </p>
                    <p
                        className="
                            text-lg
                            text-cyan-400
                            font-bold
                            tracking-normal
                        "
                    >
                        {epochTime || "1782323991.392"}
                    </p>
                </div>

                <div className="h-10 w-px bg-slate-900 mx-4" />
                <div className="pl-2">
                    <p
                        className="
                            text-[11px]
                            text-slate-400
                            font-semibold
                            tracking-widest
                            uppercase
                            mb-1.5
                        "
                    >
                        SIM MODE
                    </p>
                    <p
                        className="
                            text-lg
                            text-emerald-400
                            font-bold
                            tracking-wide
                        "
                    >
                        LIVE SYNC
                    </p>
                </div>
            </div>
        </div>
    );
}