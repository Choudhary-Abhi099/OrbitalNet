import { useState } from "react";
import { useVisualizationStore } from "../../store/useVisualizationStore";

export default function EnvironmentSettings() {
  const [atmosphereEnabled, setAtmosphereEnabled] =
    useState(false);

  const [latencyEnabled, setLatencyEnabled] =
    useState(true);

  const {
    showOrbitPaths,
    showHistoricalTrails,
    toggleOrbitPaths,
    toggleHistoricalTrails,
  } = useVisualizationStore();

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
        <span className="font-bold text-lg select-none">
          &lt;···&gt;
        </span>

        <h2 className="text-slate-300 font-bold text-base tracking-widest uppercase">
          ENVIRONMENT SETTINGS
        </h2>
      </div>

      <div className="grid grid-cols-2 gap-4">

        {/* Atmosphere */}
        <button
          onClick={() =>
            setAtmosphereEnabled(
              !atmosphereEnabled
            )
          }
          className={`
            flex items-center justify-between
            px-5 py-4 border transition-all duration-200
            ${
              atmosphereEnabled
                ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400"
                : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
            }
          `}
        >
          <span className="text-sm font-medium">
            Atmo Interf.
          </span>

          <div
            className={`
              relative w-9 h-5 rounded-full p-0.5
              ${
                atmosphereEnabled
                  ? "bg-cyan-400"
                  : "bg-slate-800"
              }
            `}
          >
            <div
              className={`
                w-4 h-4 rounded-full bg-[#0B0F17]
                transition-transform duration-200
                ${
                  atmosphereEnabled
                    ? "translate-x-4"
                    : "translate-x-0"
                }
              `}
            />
          </div>
        </button>

        {/* Ground Latency */}
        <button
          onClick={() =>
            setLatencyEnabled(
              !latencyEnabled
            )
          }
          className={`
            flex items-center justify-between
            px-5 py-4 border transition-all duration-200
            ${
              latencyEnabled
                ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400"
                : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
            }
          `}
        >
          <span className="text-sm font-medium">
            Ground Latency
          </span>

          <div
            className={`
              relative w-9 h-5 rounded-full p-0.5
              ${
                latencyEnabled
                  ? "bg-cyan-400"
                  : "bg-slate-800"
              }
            `}
          >
            <div
              className={`
                w-4 h-4 rounded-full bg-[#0B0F17]
                transition-transform duration-200
                ${
                  latencyEnabled
                    ? "translate-x-4"
                    : "translate-x-0"
                }
              `}
            />
          </div>
        </button>

        {/* Orbit Paths */}
        <button
          onClick={toggleOrbitPaths}
          className={`
            flex items-center justify-between
            px-5 py-4 border transition-all duration-200
            ${
              showOrbitPaths
                ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400"
                : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
            }
          `}
        >
          <span className="text-sm font-medium">
            Orbit Paths
          </span>

          <div
            className={`
              relative w-9 h-5 rounded-full p-0.5
              ${
                showOrbitPaths
                  ? "bg-cyan-400"
                  : "bg-slate-800"
              }
            `}
          >
            <div
              className={`
                w-4 h-4 rounded-full bg-[#0B0F17]
                transition-transform duration-200
                ${
                  showOrbitPaths
                    ? "translate-x-4"
                    : "translate-x-0"
                }
              `}
            />
          </div>
        </button>

        {/* Historical Trails */}
        <button
          onClick={toggleHistoricalTrails}
          className={`
            flex items-center justify-between
            px-5 py-4 border transition-all duration-200
            ${
              showHistoricalTrails
                ? "border-cyan-500/50 bg-cyan-950/10 text-cyan-400"
                : "border-slate-900 bg-[#121620]/40 text-slate-400 hover:text-slate-300"
            }
          `}
        >
          <span className="text-sm font-medium">
            Historical Trails
          </span>

          <div
            className={`
              relative w-9 h-5 rounded-full p-0.5
              ${
                showHistoricalTrails
                  ? "bg-cyan-400"
                  : "bg-slate-800"
              }
            `}
          >
            <div
              className={`
                w-4 h-4 rounded-full bg-[#0B0F17]
                transition-transform duration-200
                ${
                  showHistoricalTrails
                    ? "translate-x-4"
                    : "translate-x-0"
                }
              `}
            />
          </div>
        </button>

      </div>
    </div>
  );
}