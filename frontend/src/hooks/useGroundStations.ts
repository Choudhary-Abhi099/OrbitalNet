import {
    useEffect,
    useState
} from "react";

export function useGroundStations() {

    const [
        stations,
        setStations
    ] = useState<any[]>([]);

    useEffect(() => {

        async function load() {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/ground-stations"
                );

            const data =
                await response.json();

            setStations(data);
        }

        load();

    }, []);

    return stations;
}