import { useEffect, useRef, useMemo } from "react";
import { Viewer, Entity, PolylineGraphics, ImageryLayer } from "resium";
import * as Cesium from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";
import { useSatellites } from "../../hooks/useSatellites";
import { useGroundStations } from "../../hooks/useGroundStations";
import { useRoutes } from "../../hooks/useRoutes";

Cesium.Ion.defaultAccessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3NzU3ZTk4ZS01YTliLTQ4YzItODkyNi1mMzllMGE2OWJkNTMiLCJpZCI6NDQ4NzAyLCJpc3MiOiJodHRwczovL2FwaS5jZXNpdW0uY29tIiwiYXVkIjoidW5kZWZpbmVk_default&iat=1782327430.4wnAxU2iZ59-DK5iQ0c9cgrQF9fX6-lGUU8uPX86ON4";

function makeOrbitalRing(tiltDeg: number, radiusKm: number, segments = 120): Cesium.Cartesian3[] {
  const points: Cesium.Cartesian3[] = [];
  const r = radiusKm * 1000;
  const tilt = Cesium.Math.toRadians(tiltDeg);
  for (let i = 0; i <= segments; i++) {
    const angle = (i / segments) * Math.PI * 2;
    points.push(new Cesium.Cartesian3(
      r * Math.cos(angle),
      r * Math.sin(angle) * Math.cos(tilt),
      r * Math.sin(angle) * Math.sin(tilt),
    ));
  }
  return points;
}

export default function OrbitalGlobe() {
  const satellites = useSatellites();
  const stations = useGroundStations();
  const routes = useRoutes();
  
  const viewerRef = useRef<any>(null);
  const darkImageryProvider = useMemo(() => {
    return new Cesium.UrlTemplateImageryProvider({
      url: "https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png",
      subdomains: ["a", "b", "c", "d"],
    });
  }, []);

  const hiddenCreditContainer = useMemo(() => {
    if (typeof document === "undefined") return undefined;
    const div = document.createElement("div");
    div.style.display = "none";
    return div;
  }, []);

  useEffect(() => {
    const viewer = viewerRef.current?.cesiumElement;
    if (!viewer) return;

    viewer.scene.backgroundColor = Cesium.Color.fromCssColorString("#02050a");
    
    if (viewer.scene.skyBox) viewer.scene.skyBox.show = false;
    if (viewer.scene.sun) viewer.scene.sun.show = false;
    if (viewer.scene.moon) viewer.scene.moon.show = false;

    viewer.scene.globe.baseColor = Cesium.Color.fromCssColorString("#04070e");
    viewer.scene.globe.enableLighting = false; 

    if (viewer.scene.skyAtmosphere) {
      viewer.scene.skyAtmosphere.show = true;
      viewer.scene.skyAtmosphere.hueShift = -0.6;
      viewer.scene.skyAtmosphere.saturationShift = -0.4;
      viewer.scene.skyAtmosphere.brightnessShift = -0.85; 
    }

    const bloom = viewer.scene.postProcessStages.bloom;
    if (bloom) {
      bloom.enabled = true;
      (bloom.uniforms as Record<string, unknown>).glowOnly = false;
      (bloom.uniforms as Record<string, unknown>).contrast = 115;
      (bloom.uniforms as Record<string, unknown>).brightness = -0.35;
      (bloom.uniforms as Record<string, unknown>).sigma = 2.2;
      (bloom.uniforms as Record<string, unknown>).stepSize = 1.0;
    }

    viewer.camera.setView({
      destination: Cesium.Cartesian3.fromDegrees(15, 25, 23_500_000),
    });

    const el = (sel: string) => (viewer.container as HTMLElement).querySelector(sel) as HTMLElement | null;
    [
      ".cesium-viewer-toolbar",
      ".cesium-viewer-animationContainer",
      ".cesium-viewer-timelineContainer",
      ".cesium-viewer-bottom",
    ].forEach((sel) => { const e = el(sel); if (e) e.style.display = "none"; });
  }, []);

  const satelliteMap = new Map(satellites.map((s) => [s.satellite_id, s]));
  const stationMap = new Map(stations.map((s) => [s.station_id, s]));

  return (
    <Viewer
      ref={viewerRef}
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
    >
      <ImageryLayer imageryProvider={darkImageryProvider} />

      {[{ tilt: 20, radius: 8400 }, { tilt: -45, radius: 8900 }, { tilt: 65, radius: 8600 }].map((ring, i) => (
        <Entity key={`ring-${i}`}>
          <PolylineGraphics
            positions={makeOrbitalRing(ring.tilt, ring.radius)}
            width={1}
            material={Cesium.Color.fromCssColorString("rgba(0, 180, 200, 0.18)")}
          />
        </Entity>
      ))}

      {satellites.map((sat) => (
        <Entity
          key={sat.satellite_id}
          position={Cesium.Cartesian3.fromDegrees(sat.longitude, sat.latitude, sat.altitude_km * 1000)}
          point={{
            pixelSize: 4,
            color: Cesium.Color.fromCssColorString("#00e5ff"),
            outlineColor: Cesium.Color.fromCssColorString("rgba(0, 229, 255, 0.2)"),
            outlineWidth: 2,
          }}
        />
      ))}

      {stations.map((station) => (
        <Entity
          key={station.station_id}
          position={Cesium.Cartesian3.fromDegrees(station.longitude, station.latitude, 0)}
          point={{
            pixelSize: 6,
            color: Cesium.Color.fromCssColorString("#ffd000"),
            outlineColor: Cesium.Color.fromCssColorString("rgba(255, 208, 0, 0.3)"),
            outlineWidth: 3,
          }}
          label={{
            text: station.station_id,
            scale: 0.45,
            fillColor: Cesium.Color.fromCssColorString("#a0c5e8"),
            style: Cesium.LabelStyle.FILL,
            pixelOffset: new Cesium.Cartesian2(0, -14),
            font: "500 11px monospace",
          }}
        />
      ))}
      {routes.map((route, i) => {
        const sat = satelliteMap.get(route.satellite);
        const station = stationMap.get(route.ground_station);
        if (!sat || !station) return null;
        return (
          <Entity key={`route-${i}`}>
            <PolylineGraphics
              positions={[
                Cesium.Cartesian3.fromDegrees(sat.longitude, sat.latitude, sat.altitude_km * 1000),
                Cesium.Cartesian3.fromDegrees(station.longitude, station.latitude, 0),
              ]}
              width={1}
              material={new Cesium.PolylineGlowMaterialProperty({
                glowPower: 0.25,
                color: Cesium.Color.fromCssColorString("#45f09e"),
              })}
            />
          </Entity>
        );
      })}
    </Viewer>
  );
}