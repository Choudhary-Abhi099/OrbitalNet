import { useEffect, useState } from "react";

export function useVisibilityLinks() {

  const [links, setLinks] =
    useState<any[]>([]);

  useEffect(() => {

    const fetchLinks = async () => {

      try {

        const response =
          await fetch(
            "http://localhost:8000/visibility-links"
          );

        const data =
          await response.json();

        setLinks(data);

      } catch (error) {

        console.error(
          "Visibility Links Error:",
          error
        );
      }
    };

    fetchLinks();

    const interval =
      setInterval(
        fetchLinks,
        5000
      );

    return () =>
      clearInterval(interval);

  }, []);

  return links;
}