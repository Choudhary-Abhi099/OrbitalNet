import { create } from "zustand";

interface VisualizationState {
  showOrbitPaths: boolean;
  showHistoricalTrails: boolean;

  toggleOrbitPaths: () => void;
  toggleHistoricalTrails: () => void;
}

export const useVisualizationStore =
  create<VisualizationState>((set) => ({
    showOrbitPaths: false,
    showHistoricalTrails: false,

    toggleOrbitPaths: () =>
      set((state) => ({
        showOrbitPaths:
          !state.showOrbitPaths,
      })),

    toggleHistoricalTrails: () =>
      set((state) => ({
        showHistoricalTrails:
          !state.showHistoricalTrails,
      })),
  }));