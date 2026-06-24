import Navbar from "../components/layouts/Navbar";
import NetworkOverview from "../components/dashboard/NetworkOverview";
import DashboardHeader from "../components/layouts/DashboardHeader";
import { useSimulationSocket } from "../hooks/useSimulationSocket";
import ConstellationDensity from "../components/dashboard/ConstellationDensity";
import VisualizationPanel from "../components/dashboard/VisualizationPanel";
import EnvironmentSettings from "../components/dashboard/EnvironmentSettings";
import StatusPanel from "../components/dashboard/StatusPanel";
import AdvancedTools from "../components/dashboard/AdvancedTools";
import BottomNavigation from "../components/layouts/BottomNavigation";

export default function Dashboard() {
  const dashboardData = useSimulationSocket();

  if (!dashboardData) {
    return (
      <div className="p-10 text-white bg-[#0b111e] bg-[radial-gradient(#1e293b_1px,transparent_1px)] bg-size-[50px_50px] min-h-screen">
        Connecting...
      </div>
    );
  }

  return (
    <>
      <Navbar />
      <div
        className="
          min-h-screen
          bg-[#0A0D13] 
          bg-[radial-gradient(#1e293b_1px,transparent_1px)] 
          bg-size-[40px_40px]
          text-white
          px-10 py-5
        "
      >
        <DashboardHeader />

        <div
          className="
            grid
            grid-cols-12
            gap-4
            mt-8
          "
        >
          <div className="col-span-3 space-y-6">
            <NetworkOverview
              satellites={dashboardData.network.satellites}
              links={dashboardData.network.links}
              averageDegree={dashboardData.network.average_degree}
            />

            <ConstellationDensity
              activeSatellites={dashboardData.network.satellites}
            />
          </div>

          <div className="col-span-6 space-y-6">
            <VisualizationPanel
              satellites={dashboardData.network.satellites}
              links={dashboardData.network.links}
            />

            <EnvironmentSettings />
          </div>

          <div className="col-span-3 space-y-6">
            <StatusPanel />

            <AdvancedTools />
          </div>
        </div>

        <BottomNavigation />
      </div>
    </>
  );
}
