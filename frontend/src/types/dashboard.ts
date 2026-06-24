export interface DashboardPayload {

    network: {

        satellites: number;

        links: number;

        average_degree: number;
    };

    connectivity: {

        user_id: string;

        connected_satellite: string;

        ground_station: string;

        status: string;
    };

    communication: {

        status: string;

        rssi: number;

        snr: number;

        latency: number;

        packet_loss: number;
    };
}