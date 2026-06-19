# IRIV_COMPRESSOR

Industrial Compressor Monitoring System using **RS485 Modbus RTU communication**, providing real-time monitoring, data logging, and dashboard visualization for compressor performance, energy consumption, and predictive maintenance.

---

## Features

- Pressure & Temperature Monitoring
- Flow Meter Monitoring
- 3-Phase Electrical Parameter Monitoring
- Environmental Temperature & Humidity Monitoring
- Vibration Monitoring
- Energy Consumption Monitoring
- Database Logging
- Real-Time Dashboard Visualization
- RS485 Modbus RTU Communication
- Industrial Data Acquisition System

---

## System Architecture

```text
Industrial Sensors
        │
        ▼
 RS485 Modbus RTU Network
        │
        ▼
      IRIV PiControl
 (Node-RED Application)
        │
 ┌──────┴────────┐
 ▼               ▼
Dashboard      Database
Visualization  Data Logging
        │
        ▼
Performance Monitoring &
Predictive Maintenance
```

---

## System Overview

This project integrates multiple industrial sensors into a centralized monitoring platform built on **IRIV PiControl** and **Node-RED**.

Sensor data are acquired through **RS485 Modbus RTU communication**, processed in real time, and displayed on a dashboard while simultaneously being stored for historical analysis. The system enables compressor performance monitoring, environmental monitoring, energy analysis, and predictive maintenance.

---

## Main Data Flow

```text
Sensors
   │
   ▼
RS485 Modbus RTU
   │
   ▼
IRIV PiControl
(Node-RED)
   │
   ├── Data Processing
   ├── Byte Conversion
   ├── Scaling & Calculation
   ├── Average Calculation
   │
   ├────────► Dashboard Visualization
   │
   └────────► Database Logging
                     │
                     ▼
            Historical Data Analysis
                     │
                     ▼
             Predictive Maintenance
```

---

## Sensors Used

| RS485 ID | Device | Parameters |
|----------|---------|------------|
| 1 | Pressure & Temperature Sensor (PD500) | Pressure, Temperature |
| 2 | Temperature & Humidity Sensor (Blower) | Ambient Temperature, Humidity |
| 3 | Temperature & Humidity Sensor (Environment) | Ambient Temperature, Humidity |
| 4 | Temperature & Humidity Sensor (Compressor Chamber) | Ambient Temperature, Humidity |
| 5 | Thermocouple Sensor (Motor Compressor) | Ambient Temperature, Humidity |
| 11 | Flow Meter | Flow Rate, Flow Velocity |
| 12 | ADL400N Three-Phase Power Meter | Voltage, Current, Power, Power Factor, Frequency, Energy |
| 80 | Vibration Sensor | Machine Vibration |

---

## Parameters Monitored

### Process Monitoring
- Pressure
- Temperature
- Flow Rate
- Flow Velocity

### Environmental Monitoring
- Temperature
- Relative Humidity

### Electrical Monitoring
- Phase Voltage (L1, L2, L3)
- Line Voltage (AB, BC, CA)
- Current (L1, L2, L3)
- Average Voltage
- Average Current
- Total Power
- Power Factor
- Frequency
- Total Energy Consumption

### Condition Monitoring
- Vibration Level

---

## Software Stack

- Node-RED
- IRIV PiControl
- Modbus RTU
- RS485 Communication
- Dashboard UI
- Database Logging

---

## Applications

- Industrial Compressor Monitoring
- Condition Monitoring
- Energy Consumption Analysis
- Equipment Performance Monitoring
- Historical Data Logging
- Predictive Maintenance
- Industrial Internet of Things (IIoT)

---

## Project Objectives

- Monitor compressor operating conditions in real time.
- Collect and store sensor data continuously.
- Analyze electrical energy consumption.
- Detect abnormal machine behavior through vibration monitoring.
- Improve maintenance planning through historical data analysis.
- Increase system reliability and operational efficiency.

---

## Hardware Components

- IRIV PiControl
- Pressure & Temperature Sensor (PD500)
- Temperature & Humidity Sensors (×3)
- Flow Meter
- ADL400N Three-Phase Power Meter
- Vibration Sensor
- RS485 Communication Network

---

## Technologies

- Node-RED
- RS485
- Modbus RTU
- Industrial Sensors
- Dashboard Visualization
- Database Logging
- Industrial Internet of Things (IIoT)

---

## Purpose

Designed for:

- Industrial Monitoring
- Compressor Performance Monitoring
- Predictive Maintenance
- Energy Consumption Analysis
- Real-Time Data Logging
- Industrial IoT Applications

---

Link to login to NodeRed for coding:
192.168.1.41:1880
user: admin
password: iriv_compressor

Link to login to NodeRed Dashboard for monitoring:
192.168.1.41:1880/ui

Link to login into the database:
192.168.1.41/phpmyadmin
user: root
password: raspberry

---
