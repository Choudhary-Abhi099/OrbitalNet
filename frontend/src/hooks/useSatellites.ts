import {
    useEffect,
    useState
} from "react";

export function useSatellites() {

    const [
        satellites,
        setSatellites
    ] = useState<any[]>([]);

    useEffect(() => {

        async function load() {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/satellites"
                );

            const data =
                await response.json();

            setSatellites(data);
        }

        load();

        const interval =
            setInterval(
                load,
                5000
            );

        return () =>
            clearInterval(
                interval
            );

    }, []);

    return satellites;
}