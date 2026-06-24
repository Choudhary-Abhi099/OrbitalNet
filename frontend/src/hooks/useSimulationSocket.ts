import { useEffect, useState } from "react";

// import type {
//     NetworkStats
// } from "../types/network";
import type { DashboardPayload } from "../types/dashboard";

export function useSimulationSocket() {

    const [dashboardData, setDashboardData] =
        useState<DashboardPayload | null>(
            null
        );

    useEffect(() => {

        const socket =
            new WebSocket(
                "ws://127.0.0.1:8000/ws/simulation"
            );

        socket.onmessage = (
            event
        ) => {

            const data =
                JSON.parse(
                    event.data
                );

            setDashboardData(data);
        };

        return () => {

            socket.close();
        };

    }, []);

    return dashboardData;
}