import { useEffect, useState } from "react";
type TelemetryEventTuple = [string | number, string, string];

const getEventColor = (eventType: string) => {
    switch (eventType) {
        case "LINK_RECOVERED":
        case "NOMINAL OPERATION":
            return "text-emerald-400";
        case "LOW_SNR":
            return "text-amber-400";
        case "LINK_DOWN":
        case "SATELLITE_FAILED":
            return "text-rose-400";
        default:
            return "text-slate-400";
    }
};

export default function EventLog() {
    const [events, setEvents] = useState<TelemetryEventTuple[]>([]);

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await fetch("http://127.0.0.1:8000/telemetry/latest");
                const data = await response.json();
                setEvents(data.slice(0, 3));
            } catch (err) {
                console.error("Telemetry fetch failed, using UI fallback matrix:", err);
                setEvents([
                    [1, "NOMINAL OPERATION", "T+12:44:02.1"],
                    [2, "CALIBRATION COMPLETE", "T+11:20:00.0"]
                ]);
            }
        };

        fetchEvents();
        const interval = setInterval(fetchEvents, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="w-full text-left">
            <h3 className="text-slate-500 font-bold text-xs tracking-[0.15em] uppercase mb-5">
                ACTIVE EVENTS LOG
            </h3>

            <div className="space-y-4">
                {events.map((event) => {
                    const eventType = event[1] || "NOMINAL OPERATION";
                    const timestamp = event[2] || "T+00:00:00.0";
                    const colorClass = getEventColor(eventType);
                    const isMuted = eventType === "CALIBRATION COMPLETE";
                    
                    return (
                        <div key={event[0]} className="flex flex-col gap-0.5 pl-1">
                            <div className={`flex items-center gap-2 text-[13px] font-mono font-bold tracking-wide uppercase ${isMuted ? "text-slate-500" : colorClass}`}>
                                <span className="text-[9px] scale-90">●</span>
                                <span>{eventType}</span>
                            </div>
                            <div className="text-[11px] font-mono text-slate-500 font-medium pl-3.5 tracking-normal">
                                {timestamp}
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}