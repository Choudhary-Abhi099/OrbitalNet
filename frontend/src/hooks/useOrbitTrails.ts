import { useEffect, useState } from "react";

export function useOrbitTrails() {
  const [trails, setTrails] = useState<Record<string, any[]>>({});

  useEffect(() => {
    const fetchTrails = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/orbit-trails"
        );

        const data = await response.json();

        setTrails(data);
      } catch (error) {
        console.error(
          "Failed to fetch orbit trails",
          error
        );
      }
    };

    fetchTrails();

    const interval = setInterval(
      fetchTrails,
      5000
    );

    return () => clearInterval(interval);
  }, []);

  return trails;
}