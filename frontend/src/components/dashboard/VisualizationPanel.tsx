import { Video, Search, RotateCcw } from "lucide-react";
import OrbitalGlobe from "../globe/OrbitalGlobe";

interface Props {
  avgLatency?: number;
}

export default function VisualizationPanel({
  avgLatency = 42,
}: Props) {
  return (
    <div className="w-full h-162.5 rounded-sm border border-[#112233] relative overflow-hidden bg-[#04070a] select-none">
      
      <OrbitalGlobe />
      <div className="absolute top-6 left-6 z-10 flex items-center gap-2 bg-[#040a10]/85 border border-[#163555]/70 px-3 py-2 rounded-xs backdrop-blur-sm">
        <div className="text-[#56f099] flex items-center justify-center">
          <Video size={13} fill="#56f099" />
        </div>
        <h2 className="text-[#ecf0f5] uppercase tracking-[0.15em] text-[11px] font-bold font-mono">
          Visualizer_V2.4
        </h2>
      </div>
      <div
        className="absolute bottom-6 left-6 z-10 pointer-events-none"
        style={{
          background: "rgba(4, 10, 16, 0.85)",
          border: "1px solid rgba(22, 53, 85, 0.7)",
          borderRadius: 2,
          padding: "14px 20px",
          boxShadow: "0 8px 32px rgba(0,0,0,0.6)",
          backdropFilter: "blur(4px)"
        }}
      >
        <div style={{ fontFamily: "monospace", fontSize: 10, letterSpacing: "0.15em", color: "#6080a0", marginBottom: 6, fontWeight: 600 }}>
          LATENCY (GROUND-NODE)
        </div>
        <div style={{ fontFamily: "monospace", fontSize: 24, fontWeight: 700, color: "#56f099", textShadow: "0 0 10px rgba(86,240,153,0.3)" }}>
          {avgLatency}ms <span className="text-xs font-normal text-[#507090]">avg</span>
        </div>
      </div>
      <div className="absolute bottom-6 right-6 z-10 flex gap-2">
        <button
          style={{
            background: "rgba(4, 10, 16, 0.85)",
            border: "1px solid rgba(22, 53, 85, 0.7)",
            borderRadius: 2,
            color: "#a0c0e0",
            width: 36,
            height: 36,
            cursor: "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 0.15s ease"
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = "#56f099";
            e.currentTarget.style.color = "#ffffff";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = "rgba(22, 53, 85, 0.7)";
            e.currentTarget.style.color = "#a0c0e0";
          }}
        >
          <Search size={15} />
        </button>
        <button
          style={{
            background: "rgba(4, 10, 16, 0.85)",
            border: "1px solid rgba(22, 53, 85, 0.7)",
            borderRadius: 2,
            color: "#a0c0e0",
            width: 36,
            height: 36,
            cursor: "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 0.15s ease"
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = "#56f099";
            e.currentTarget.style.color = "#ffffff";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = "rgba(22, 53, 85, 0.7)";
            e.currentTarget.style.color = "#a0c0e0";
          }}
        >
          <RotateCcw size={15} />
        </button>
      </div>

    </div>
  );
}