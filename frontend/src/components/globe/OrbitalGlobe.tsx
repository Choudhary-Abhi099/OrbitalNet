import { useState, useMemo } from "react";
import { Viewer, Entity, PolylineGraphics, Globe } from "resium";
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";
import { useSatellites } from "../../hooks/useSatellites";
import { useGroundStations } from "../../hooks/useGroundStations";
import { useRoutes } from "../../hooks/useRoutes";
import { useOrbitTrails } from "../../hooks/useOrbitTrails";
import { useOrbitPaths } from "../../hooks/useOrbitPaths";
import { useVisualizationStore } from "../../store/useVisualizationStore";
import { useVisibilityLinks } from "../../hooks/useVisibilityLinks";
Cesium.Ion.defaultAccessToken =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3NzU3ZTk4ZS01YTliLTQ4YzItODkyNi1mMzllMGE2OWJkNTMiLCJpZCI6NDQ4NzAyLCJpc3MiOiJodHRwczovL2FwaS5jZXNpdW0uY29tIiwiYXVkIjoidW5kZWZpbmVkX2RlZmF1bHQiLCJpYXQiOjE3ODIzMjc0MzB9.4wnAxU2iZ59-DK5iQ0c9cgrQF9fX6-lGUU8uPX86ON4";
export default function OrbitalGlobe() {
  const satellites = useSatellites();
  const stations = useGroundStations();
  const routes = useRoutes();
  const visibilityLinks = useVisibilityLinks();
  const trails = useOrbitTrails();
  const paths = useOrbitPaths();
  const [viewerInstance, setViewerInstance] = useState<any | null>(null);
  const [hoveredSatellite, setHoveredSatellite] = useState<string | null>(null);

  const showOrbitPaths = useVisualizationStore((state) => state.showOrbitPaths);
  const showHistoricalTrails = useVisualizationStore(
    (state) => state.showHistoricalTrails,
  );
  const hoveredPathPoints = useMemo(() => {
    if (!hoveredSatellite || !paths[hoveredSatellite]) return [];
    const rawPoints = paths[hoveredSatellite];
    return rawPoints;
  }, [hoveredSatellite, paths]);
  const hoveredVisibilityLink = useMemo(() => {
    if (!hoveredSatellite) {
      return null;
    }

    return visibilityLinks.find((link) => link.satellite === hoveredSatellite);
  }, [hoveredSatellite, visibilityLinks]);
  const hiddenCreditContainer = useMemo(() => {
    if (typeof document === "undefined") return undefined;
    const div = document.createElement("div");
    div.style.display = "none";
    return div;
  }, []);

  const initializeCesiumScene = (instance: any) => {
    if (!instance || viewerInstance) return;
    setViewerInstance(instance);

    const viewer = instance.cesiumElement;
    if (!viewer) return;
    viewer.imageryLayers.removeAll();
    viewer.imageryLayers.addImageryProvider(
      new Cesium.UrlTemplateImageryProvider({
        url: "https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png",
        subdomains: ["a", "b", "c", "d"],
      }),
    );

    viewer.scene.backgroundColor = Cesium.Color.TRANSPARENT;
    if (viewer.scene.skyBox) viewer.scene.skyBox.show = false;
    if (viewer.scene.sun) viewer.scene.sun.show = false;
    if (viewer.scene.moon) viewer.scene.moon.show = false;

    const bloom = viewer.scene.postProcessStages.bloom;
    if (bloom) bloom.enabled = false;

    viewer.camera.setView({
      destination: Cesium.Cartesian3.fromDegrees(15, 25, 23_500_000),
    });

    const el = (sel: string) =>
      (viewer.container as HTMLElement).querySelector(
        sel,
      ) as HTMLElement | null;
    [
      ".cesium-viewer-toolbar",
      ".cesium-viewer-animationContainer",
      ".cesium-viewer-timelineContainer",
      ".cesium-viewer-bottom",
    ].forEach((sel) => {
      const e = el(sel);
      if (e) e.style.display = "none";
    });
  };

  const handleSatelliteMouseMove = (_movement: any, targetEntity: any) => {
    if (targetEntity?.id?.properties?.entityType?.getValue() === "satellite") {
      const satId = targetEntity.id.name;
      setHoveredSatellite((prev) => (prev === satId ? prev : satId));
    }
  };

  const handleViewerMouseMove = (movement: any) => {
    if (!viewerInstance?.cesiumElement) return;
    const picked = viewerInstance.cesiumElement.scene.pick(
      movement.endPosition,
    );
    if (!Cesium.defined(picked)) {
      setHoveredSatellite(null);
    }
  };

  const satelliteMap = useMemo(
    () => new Map(satellites.map((s) => [s.satellite_id, s])),
    [satellites],
  );
  const stationMap = useMemo(
    () => new Map(stations.map((s) => [s.station_id, s])),
    [stations],
  );

  return (
    <div style={{ width: "100%", height: "100%", position: "relative" }}>
      <Viewer
        ref={initializeCesiumScene}
        style={{ width: "100%", height: "100%" }}
        animation={false}
        timeline={false}
        baseLayerPicker={false}
        geocoder={false}
        homeButton={false}
        sceneModePicker={false}
        navigationHelpButton={false}
        fullscreenButton={false}
        infoBox={false}
        selectionIndicator={false}
        creditContainer={hiddenCreditContainer}
        skyBox={false}
        contextOptions={{ webgl: { alpha: true } }}
        onMouseMove={handleViewerMouseMove}
      >
        <Globe
          baseColor={Cesium.Color.fromCssColorString("#0D0D0D")}
          enableLighting={false}
          showGroundAtmosphere={false}
        />

        {satellites.map((sat) => (
          <Entity
            key={sat.satellite_id}
            name={sat.satellite_id}
            properties={new Cesium.PropertyBag({ entityType: "satellite" })}
            position={Cesium.Cartesian3.fromDegrees(
              sat.longitude,
              sat.latitude,
              sat.altitude_km * 1000,
            )}
            onMouseMove={handleSatelliteMouseMove}
            point={{
              pixelSize: hoveredSatellite === sat.satellite_id ? 10 : 8,
              color:
                hoveredSatellite === sat.satellite_id
                  ? Cesium.Color.WHITE
                  : Cesium.Color.fromCssColorString("#00e5ff"),
              outlineColor: Cesium.Color.fromCssColorString(
                "rgba(0,229,255,0.2)",
              ),
              outlineWidth: 2,
            }}
            label={
              hoveredSatellite === sat.satellite_id
                ? {
                    text: sat.satellite_id,
                    scale: 0.7,
                    fillColor: Cesium.Color.WHITE,
                    showBackground: true,
                    backgroundColor: Cesium.Color.BLACK.withAlpha(0.75),
                    pixelOffset: new Cesium.Cartesian2(0, -20),
                  }
                : undefined
            }
          />
        ))}

        {showOrbitPaths && hoveredSatellite && hoveredPathPoints.length > 1 && (
          <Entity key={`path-${hoveredSatellite}`}>
            <PolylineGraphics
              positions={hoveredPathPoints.map((point: any) =>
                Cesium.Cartesian3.fromDegrees(
                  point.longitude,
                  point.latitude,
                  point.altitude_km * 1000,
                ),
              )}
              width={3}
              material={Cesium.Color.fromCssColorString("#4fc3f7").withAlpha(
                0.6,
              )}
            />
          </Entity>
        )}

        {showHistoricalTrails &&
          Object.entries(trails).map(([satelliteId, positions]) => {
            if (!Array.isArray(positions) || positions.length < 2) return null;
            return (
              <Entity key={`trail-${satelliteId}`}>
                <PolylineGraphics
                  positions={positions.map((point: any) =>
                    Cesium.Cartesian3.fromDegrees(
                      point.longitude,
                      point.latitude,
                      point.altitude_km * 1000,
                    ),
                  )}
                  width={3}
                  material={
                    new Cesium.PolylineGlowMaterialProperty({
                      glowPower: 0.15,
                      color: Cesium.Color.CYAN,
                    })
                  }
                />
              </Entity>
            );
          })}

        {stations.map((station) => (
          <Entity
            key={station.station_id}
            position={Cesium.Cartesian3.fromDegrees(
              station.longitude,
              station.latitude,
              0,
            )}
            point={{
              pixelSize: 6,
              color: Cesium.Color.fromCssColorString("#ffd000"),
              outlineColor: Cesium.Color.fromCssColorString(
                "rgba(255, 208, 0, 0.3)",
              ),
              outlineWidth: 3,
            }}
            label={{
              text: station.station_id,
              scale: 1,
              fillColor: Cesium.Color.fromCssColorString("#a0c5e8"),
              style: Cesium.LabelStyle.FILL,
              pixelOffset: new Cesium.Cartesian2(0, -14),
              font: "500 11px monospace",
            }}
          />
        ))}
        {visibilityLinks.map((link, index) => {
          const sat = satelliteMap.get(link.satellite);

          const station = stationMap.get(link.ground_station);

          if (!sat || !station) {
            return null;
          }

          return (
            <Entity key={`visibility-${index}`}>
              <PolylineGraphics
                positions={[
                  Cesium.Cartesian3.fromDegrees(
                    sat.longitude,
                    sat.latitude,
                    sat.altitude_km * 1000,
                  ),

                  Cesium.Cartesian3.fromDegrees(
                    station.longitude,
                    station.latitude,
                    0,
                  ),
                ]}
                width={1}
                material={
                  new Cesium.PolylineGlowMaterialProperty({
                    glowPower: 0.05,

                    color:
                      Cesium.Color.fromCssColorString("#4fc3f7").withAlpha(
                        0.15,
                      ),
                  })
                }
              />
            </Entity>
          );
        })}
        {routes.map((route, i) => {
          const sat = satelliteMap.get(route.satellite);
          const station = stationMap.get(route.ground_station);
          if (!sat || !station) return null;
          return (
            <Entity key={`route-${i}`}>
              <PolylineGraphics
                positions={[
                  Cesium.Cartesian3.fromDegrees(
                    sat.longitude,
                    sat.latitude,
                    sat.altitude_km * 1000,
                  ),
                  Cesium.Cartesian3.fromDegrees(
                    station.longitude,
                    station.latitude,
                    0,
                  ),
                ]}
                width={1}
                material={
                  new Cesium.PolylineGlowMaterialProperty({
                    glowPower: 0.25,
                    color: Cesium.Color.fromCssColorString("#45f09e"),
                  })
                }
              />
            </Entity>
          );
        })}
      </Viewer>
      {hoveredSatellite && hoveredVisibilityLink && (
        <div
          className="
        absolute
        top-4
        right-4
        z-50
        bg-[#0B0F17]
        border
        border-cyan-500/30
        p-4
        rounded
        text-xs
        font-mono
        text-slate-300
        shadow-lg
      "
        >
          <div className="text-cyan-400 mb-2 font-bold">{hoveredSatellite}</div>

          <div>Ground Station:</div>

          <div className="text-white">
            {hoveredVisibilityLink.ground_station}
          </div>

          <div className="mt-2">Distance:</div>

          <div className="text-green-400">
            {Math.round(hoveredVisibilityLink.distance_km)} km
          </div>
        </div>
      )}
    </div>
  );
}
