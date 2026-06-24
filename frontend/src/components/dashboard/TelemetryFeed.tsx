import { useEffect, useState } from "react";

import type { TelemetryEvent } from "../../types/telemetry";
const getEventColor = (eventType: string) => {
  switch (eventType) {
    case "LINK_RECOVERED":
      return "text-green-400";

    case "LOW_SNR":
      return "text-yellow-400";

    case "LINK_DOWN":
    case "SATELLITE_FAILED":
      return "text-red-400";

    default:
      return "text-white";
  }
};
export default function TelemetryFeed() {
  const [events, setEvents] = useState<TelemetryEvent[]>([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await fetch("http://127.0.0.1:8000/telemetry/latest");

      const data = await response.json();

      setEvents(data);
    };

    fetchEvents();

    const interval = setInterval(fetchEvents, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div
      className="
               bg-slate-800
    rounded-xl
    p-6
    border
    border-cyan-900
    min-h-150
            "
    >
      <h2
        className="
                    text-xl
                    font-bold
                    mb-4
                "
      >
        Live Telemetry Feed
      </h2>

      <div
        className="
                    space-y-2
                "
      >
        {events.map((event) => (
          <div
            key={event[0]}
            className="
                                border-b
                                border-slate-700
                                pb-2
                            "
          >
            <div
              className={`
        font-semibold
        ${getEventColor(event[1])}
    `}
            >
              {event[1]}
            </div>

            <div
              className="
                                    text-sm
                                    text-gray-400
                                "
            >
              {event[2]}
            </div>

            <div
              className="
                                    text-sm
                                "
            >
              {event[3]}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
