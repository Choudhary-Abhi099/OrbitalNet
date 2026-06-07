# 🌍 OrbitalNet

### Starlink-Inspired Satellite Network Simulator

OrbitalNet is a large-scale satellite communication and network simulation platform inspired by modern Low Earth Orbit (LEO) constellations such as Starlink.

The project combines **Distributed Systems Engineering**, **Satellite Communication**, **Network Routing**, **Signal Processing**, and **Real-Time Visualization** to simulate how satellite internet systems operate in the real world.

OrbitalNet models satellites, ground stations, users, communication links, routing decisions, telemetry streams, coverage zones, signal quality, network failures, and communication reliability.

---

# 🚀 Project Vision

Modern satellite internet networks contain thousands of satellites that continuously move around Earth while maintaining communication with users and ground stations.

OrbitalNet aims to simulate:

- LEO Satellite Constellations
- Satellite-to-Satellite Communication
- Satellite-to-Ground Station Communication
- User Connectivity
- Dynamic Routing
- Signal Propagation
- Link Budget Analysis
- Telemetry Monitoring
- Network Failures
- Weather Effects
- Communication Reliability

The goal is to build a realistic environment for studying next-generation satellite internet systems.

---

# 🎯 Objectives

- Simulate large-scale satellite constellations
- Model realistic communication links
- Implement dynamic routing algorithms
- Analyze communication quality
- Visualize satellite movement in real time
- Study network resilience and fault tolerance
- Evaluate communication reliability under varying conditions

---

# 🏗️ System Architecture

```text
Users
   │
   ▼
Satellites
   │
   ▼
Inter-Satellite Links
   │
   ▼
Ground Stations
   │
   ▼
Internet Backbone

          │
          ▼

Control Center Dashboard
```

---

# 📂 Project Structure

```text
OrbitalNet/

├── backend/
├── simulation/
├── frontend/
├── visualization/
├── analytics/
├── database/
├── communication_system/
├── integration/
├── deployment/
└── docs/
```

---

# 🖥️ Software & Distributed Systems Layer

Responsible for:

- Routing
- Telemetry
- Event Processing
- Distributed Services
- Real-Time Monitoring
- Dashboard Infrastructure

## Backend

```text
backend/
├── api/
├── websocket/
├── services/
└── main.py
```

### Features

- REST APIs
- WebSocket Streaming
- Telemetry Ingestion
- Event Processing
- User Management

---

## Simulation Engine

```text
simulation/
```

### Orbital Simulation

```text
orbital/
├── orbit_propagator.py
├── tle_loader.py
├── satellite.py
└── constellation_manager.py
```

Responsible for:

- Satellite Position Updates
- Orbital Propagation
- Constellation Management

---

### Routing Engine

```text
routing/
├── graph_builder.py
├── shortest_path.py
├── handover.py
└── load_balancer.py
```

Features:

- Dynamic Routing
- Dijkstra Routing
- A* Routing
- User Handovers
- Load Balancing
- Failover Handling

---

### Scheduler

```text
scheduler/
├── simulation_clock.py
└── event_scheduler.py
```

Responsible for:

- Simulation Time
- Event Execution
- Scheduled Updates

---

# 📡 Communication Systems Layer

Responsible for:

- Communication Modeling
- Signal Analysis
- RF Calculations
- Communication Reliability

---

## Communication Engine

```text
communication_engine/
```

Models:

- User ↔ Satellite
- Satellite ↔ Satellite
- Satellite ↔ Ground Station

Communication Links

---

## Coverage Analysis

```text
coverage_analysis/
```

Calculates:

- Coverage Radius
- Visibility
- Elevation Angle
- Service Regions

---

## Propagation Engine

```text
propagation_engine/
```

Models:

- Free Space Path Loss
- Signal Attenuation
- RF Propagation

---

## Link Budget

```text
link_budget/
```

Calculates:

- Transmit Power
- Receiver Gain
- Path Loss
- Link Margin
- Received Signal Strength

---

## Weather Models

```text
weather_models/
```

Simulates:

- Rain Fade
- Atmospheric Attenuation
- Cloud Effects

---

## Signal Metrics

```text
signal_metrics/
```

Tracks:

- RSSI
- SNR
- BER
- Packet Loss
- Latency

---

## Channel Models

```text
channel_models/
```

Implements:

- AWGN
- Fading Models
- Noise Sources

---

## Modulation & Coding

```text
modulation_coding/
```

Supports:

- BPSK
- QPSK
- QAM
- OFDM
- Turbo Coding
- LDPC

---

## Doppler Analysis

```text
doppler_analysis/
```

Calculates:

- Relative Velocity
- Doppler Shift
- Frequency Offset

---

# 🔗 Integration Layer

```text
integration/
├── telemetry_adapter.py
├── communication_adapter.py
├── routing_adapter.py
└── event_bus.py
```

Purpose:

Connects communication-system outputs with routing and telemetry services.

Example:

```text
Signal Degradation
        │
        ▼
Communication Metrics
        │
        ▼
Routing Decision
        │
        ▼
Traffic Re-routing
```

---

# 📊 Analytics Layer

```text
analytics/
├── coverage_statistics.py
├── network_availability.py
├── outage_analysis.py
└── report_generator.py
```

Provides:

- Coverage Reports
- Network Availability
- Outage Analysis
- Communication Reliability Metrics

---

# 🌎 Visualization Layer

```text
visualization/
├── cesium/
├── orbit_renderer.py
├── satellite_renderer.py
└── route_renderer.py
```

Features:

- 3D Earth Visualization
- Satellite Tracking
- Coverage Maps
- Route Visualization
- Real-Time Telemetry

---

# 💾 Database Layer

```text
database/
├── telemetry.db
└── models.py
```

Stores:

- Telemetry Data
- Satellite States
- Routing Information
- Historical Analytics

---

# ⚙️ Technology Stack

## Backend

- Python
- FastAPI
- WebSockets
- Redis
- PostgreSQL

## Frontend

- React
- TypeScript
- CesiumJS

## Communication & Analysis

- Python
- MATLAB
- NumPy
- Pandas

## Visualization

- CesiumJS
- WebGL

---

# 📈 Planned Features

## Phase 1

- Satellite Simulation
- Ground Stations
- User Connections
- Coverage Analysis

## Phase 2

- Signal Propagation
- Link Budget Analysis
- Communication Metrics

## Phase 3

- Routing Engine
- Dynamic Handovers
- Network Failures

## Phase 4

- Real-Time Dashboard
- Telemetry Visualization

## Phase 5

- Weather Effects
- Doppler Analysis
- Modulation & Coding Models

## Phase 6

- AI-Based Routing Optimization
- Congestion Prediction
- Traffic Forecasting

---

# 🎓 Learning Areas

OrbitalNet covers concepts from:

### Distributed Systems

- Event-Driven Architecture
- Real-Time Systems
- Fault Tolerance
- Distributed Routing

### Computer Networks

- Routing Algorithms
- Network Topologies
- Communication Protocols

### Satellite Communication

- Link Budgets
- Coverage Analysis
- Doppler Shift
- RF Propagation

### Signal Processing

- SNR Analysis
- BER Analysis
- Channel Modeling

### Aerospace Systems

- Orbital Mechanics
- Constellation Management
- Satellite Visibility

---

# 🤝 Contributors

### Sahil Choudhary

Software Engineering & Distributed Systems

Responsible for:

- Backend Services
- Routing Engine
- Telemetry Infrastructure
- Real-Time Monitoring
- Distributed Architecture

### Abhishek

Electronics & Communication Engineering

Responsible for:

- Communication Modeling
- Signal Analysis
- Link Budget Calculations
- RF Propagation
- Coverage Analysis
- Communication Reliability

---

# 📜 License

This project is being developed for educational, research, and portfolio purposes.

---

### "Simulating the Future of Global Satellite Connectivity."
