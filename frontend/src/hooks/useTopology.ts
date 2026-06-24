import {
    useEffect,
    useState
} from "react";

import type {
    TopologyResponse
} from "../types/topology";

export function useTopology() {

    const [
        topology,
        setTopology
    ] = useState<
        TopologyResponse | null
    >(null);

    useEffect(() => {

        async function load() {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/network/topology"
                );

            const data =
                await response.json();

            setTopology(data);
        }

        load();

    }, []);

    return topology;
}