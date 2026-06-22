# OrbitalNet Architecture

## High-Level Architecture

```text
TLE Data
    │
    ▼
Orbit Propagator
    │
    ▼
Constellation Manager
    │
    ▼
Position Update Service
    │
    ▼
Simulation Clock
    │
    ▼
Event Bus
    │
    ▼
CONSTELLATION_UPDATED
    │
    ▼
Graph Builder
    │
    ▼
Network State Service
    │
    ▼
FastAPI
```

---

## Simulation Layer

### Components

* Satellite
* SatelliteFactory
* TLELoader
* OrbitPropagator
* ConstellationManager
* PositionUpdateService
* SimulationClock

### Flow

```text
TLE File
    ▼
Satellite Objects
    ▼
Orbit Propagation
    ▼
Position Updates
```

---

## Routing Layer

### Components

* DistanceCalculator
* GraphBuilder
* ShortestPathRouter
* SatelliteRouteManager
* FaultToleranceManager

### Flow

```text
Satellite Positions
       ▼
Graph Builder
       ▼
Network Graph
       ▼
Shortest Path Router
       ▼
Route
```

---

## User Layer

### Components

* UserTerminal
* BestSatelliteSelector
* UserConnectionManager

### Flow

```text
User
   ▼
Best Satellite
   ▼
Network Route
```

---

## Ground Station Layer

### Components

* GroundStation
* GroundStationManager

### Flow

```text
Satellite
    ▼
Ground Station
```

---

## Event-Driven Layer

### Components

* EventBus
* EventHandlers
* RoutingAdapter
* TelemetryAdapter
* CommunicationAdapter

### Event Flow

```text
Event
   ▼
EventBus
   ▼
Handler
   ▼
Adapter
   ▼
Service
```

---

## Telemetry Layer

### Components

* SQLite Database
* TelemetryRepository
* TelemetryQueryService

### Flow

```text
Event
   ▼
Telemetry Adapter
   ▼
SQLite
   ▼
Analytics
```

---

## Analytics Layer

### Components

* NetworkStatisticsService
* NetworkHealthService

### Metrics

* Satellite Count
* Link Count
* Average Degree
* Event Statistics
* Network Health

---

## Backend Layer

### FastAPI

```text
Client
   ▼
FastAPI
   ▼
Analytics Services
   ▼
Network State Service
```

### Current APIs

Telemetry APIs

* /telemetry/count
* /telemetry/events
* /telemetry/latest

Network APIs

* /network/statistics
* /network/health

---

## Continuous Simulation Loop

```text
SimulationClock Tick
          ▼
PositionUpdateService
          ▼
CONSTELLATION_UPDATED
          ▼
EventBus
          ▼
GraphBuilder
          ▼
NetworkStateService
          ▼
FastAPI
```

---

## Communication Layer Integration

Communication subsystem generates:

* Communication Reports
* RSSI
* SNR
* BER
* Packet Loss
* Latency

Integration Path:

```text
Communication Report
        ▼
CommunicationAdapter
        ▼
EventBus
        ▼
Telemetry
```

Supported Communication Events:

* LOW_SNR
* LINK_DOWN
* LINK_RECOVERED

---

## Phase 2 Architecture

```text
Simulation
      ▼
WebSocket Server
      ▼
React Dashboard
      ▼
Live Visualization
```

---

## Phase 3 Architecture

```text
Multiple Simulation Nodes
          ▼
Distributed Routing
          ▼
Go Services
          ▼
Global Satellite Network
```
