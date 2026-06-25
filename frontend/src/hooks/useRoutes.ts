import {
    useEffect,
    useState
} from "react";

export function useRoutes() {

    const [
        routes,
        setRoutes
    ] = useState<any[]>([]);

    useEffect(() => {

        async function load() {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/routes"
                );

            const data =
                await response.json();

            setRoutes(data);
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

    return routes;
}