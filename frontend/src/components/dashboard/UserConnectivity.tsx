import type {
    ConnectivityResponse
} from "../../types/connectivity";

interface Props {

    connectivity:
        ConnectivityResponse;
}
export default function UserConnectivity(
    {
        connectivity
    }: Props
) {


    return (

        <div
            className="
                 bg-slate-800
    rounded-xl
    p-6
    border
    border-cyan-900
            "
        >

            <h2
                className="
                    text-xl
                    font-bold
                    mb-4
                "
            >
                User Connectivity
            </h2>

            <div className="space-y-2">

                <p>
                    <strong>User:</strong>
                    {" "}
                    {connectivity.user_id}
                </p>

                <p>
                    <strong>Satellite:</strong>
                    {" "}
                    {connectivity.connected_satellite}
                </p>

                <p>
                    <strong>Ground Station:</strong>
                    {" "}
                    {connectivity.ground_station}
                </p>

                <p>
                    <strong>Status:</strong>
                    {" "}
                    {connectivity.status}
                </p>

            </div>

        </div>
    );
}