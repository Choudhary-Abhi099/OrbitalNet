import NetworkStats from "../components/dashboard/NetworkStats";
import Navbar from "../components/layouts/Navbar";
import NetworkOverview from "../components/dashboard/NetworkOverview";
import DashboardHeader from "../components/layouts/DashboardHeader";
import { useSimulationSocket } from "../hooks/useSimulationSocket";
import TelemetryFeed from "../components/dashboard/TelemetryFeed";
import UserConnectivity from "../components/dashboard/UserConnectivity";

import CommunicationMetrics from "../components/dashboard/CommunicationMetrics";
export default function Dashboard() {
  const dashboardData = useSimulationSocket();

  if (!dashboardData) {
    return (
      <div
        className="
                    p-10
                    text-white
                "
      >
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
                bg-slate-950
                text-white
                p-10
            "
      >
        <DashboardHeader />

        <div
          className="
          grid
          grid-cols-3
          gap-6
          mt-8
          "
        >
          <div
            className="
            col-span-1
            space-y-6
            "
          >
            <NetworkOverview
              satellites={dashboardData.network.satellites}
              links={dashboardData.network.links}
              averageDegree={dashboardData.network.average_degree}
            />

            <UserConnectivity connectivity={dashboardData.connectivity} />

            <CommunicationMetrics communication={dashboardData.communication} />
          </div>

          <div
            className="
            col-span-2
        "
          >
            <TelemetryFeed />
          </div>
        </div>
      </div>
    </>
  );
}
