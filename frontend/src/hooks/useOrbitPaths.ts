import { useEffect, useState } from "react";

export function useOrbitPaths() {
  const [paths, setPaths] = useState<
    Record<string, any[]>
  >({});

  useEffect(() => {
    const fetchPaths = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/orbit-paths"
        );

        const data = await response.json();

        setPaths(data);
      } catch (error) {
        console.error(
          "Failed to fetch orbit paths",
          error
        );
      }
    };

    fetchPaths();
  }, []);

  return paths;
}