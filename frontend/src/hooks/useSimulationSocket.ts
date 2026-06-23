import { useEffect, useState } from "react";

import type {
    NetworkStats
} from "../types/network";

export function useSimulationSocket() {

    const [stats, setStats] =
        useState<NetworkStats | null>(
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

            setStats(data);
        };

        return () => {

            socket.close();
        };

    }, []);

    return stats;
}