# ⚡ Smart Home Energy Monitoring System

<p align="center">
  <img src="images/banner.png" alt="Smart Home Energy Monitoring System" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![IoT](https://img.shields.io/badge/Domain-IoT-orange)
![Analytics](https://img.shields.io/badge/Energy-Analytics-purple)
![Status](https://img.shields.io/badge/Project-Completed-success)

</p>

---

# 📌 Project Overview

The **Smart Home Energy Monitoring System** is an industry-oriented IoT and Data Analytics project designed to monitor, analyze, and optimize household energy consumption.

The system simulates real-world smart home energy monitoring by collecting appliance-level energy usage, calculating power consumption, estimating electricity costs, generating alerts, and visualizing insights through an interactive Streamlit dashboard.

This project demonstrates concepts used in:

- Smart Homes
- Energy Management Systems (EMS)
- Building Automation Systems (BAS)
- Industrial Monitoring Platforms
- Smart Grids
- IoT Analytics Platforms

---

# 🎯 Problem Statement

Electricity bills continue to rise because homeowners often lack visibility into which appliances consume the most energy.

Without monitoring:

- Energy waste remains unnoticed
- High-power appliances operate inefficiently
- Electricity bills increase
- Carbon emissions rise

This project solves the problem by providing:

✅ Real-Time Monitoring

✅ Appliance-Level Analytics

✅ Cost Estimation

✅ Smart Recommendations

✅ Carbon Footprint Tracking

✅ Interactive Energy Dashboard

---

# 🚀 Key Features

### Energy Monitoring

- Real-Time Voltage Tracking
- Real-Time Current Monitoring
- Power Consumption Analysis
- Appliance-Wise Monitoring

### Analytics

- Daily Energy Consumption
- Appliance Ranking
- Peak Load Detection
- Cost Estimation

### Smart Dashboard

- Interactive Charts
- KPI Cards
- Appliance Distribution
- Digital Twin Visualization

### Reporting

- Energy Logs
- CSV Export
- Historical Data Analysis

### Sustainability

- Carbon Emission Tracking
- Energy Saving Recommendations

---

# 🏗 System Architecture

```text
          Appliance Data
                 │
                 ▼
       Energy Simulation Engine
                 │
                 ▼
           SQLite Database
                 │
                 ▼
        Streamlit Dashboard
                 │
     ┌───────────┼───────────┐
     ▼           ▼           ▼
 Analytics    Alerts    Reports
```

---

# 📂 Project Structure

```text
Smart-Home-Energy-Monitoring-System/
│
├── dashboard/
│   └── app.py
│
├── simulator/
│   └── data_generator.py
│
├── database/
│   ├── energy.db
│   ├── init_db.py
│   └── check_data.py
│
├── images/
│   ├── banner.png
│   ├── dashboard_home.png
│   ├── power_trend.png
│   ├── current_trend.png
│   ├── appliance_distribution.png
│   ├── digital_twin.png
│   └── energy_logs.png
│
├── reports/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Streamlit | Dashboard |
| SQLite | Data Storage |
| Pandas | Data Processing |
| Plotly | Interactive Visualizations |
| NumPy | Numerical Calculations |
| IoT Simulation | Virtual Smart Home |

---

# 📊 Dashboard Modules

## 1️⃣ KPI Analytics
<img width="1781" height="786" alt="P4 O s1" src="https://github.com/user-attachments/assets/92cb116d-bfa6-407b-a72c-73927b6dc53b" />

Displays:

- Total Energy Usage
- Electricity Cost
- Average Voltage
- Active Appliances
- Peak Appliance
- Carbon Emissions

---

## 📅 Daily Energy Consumption

<img width="1907" height="827" alt="P4 O s2" src="https://github.com/user-attachments/assets/c19c4eb8-156f-4b1b-92df-bab285f0bf20" />

## Power Consumption Trend

Tracks appliance power usage over time.

<img width="1561" height="711" alt="P4 O s3" src="https://github.com/user-attachments/assets/6a1d88f9-ded4-46c4-9c6a-d2db198a105d" />

<img width="1885" height="632" alt="P4 O s4" src="https://github.com/user-attachments/assets/fddd5f3c-f66a-45e3-a674-96450394fc79" />

---

## Current Consumption Trend

Monitors current drawn by appliances.

<img width="1520" height="722" alt="P4 O s5" src="https://github.com/user-attachments/assets/c721b475-7ce0-48f2-a170-f17bde32b084" />

---

## 4️⃣ Appliance Distribution

Visualizes appliance-wise power contribution.

<img width="1800" height="747" alt="P4 O s6" src="https://github.com/user-attachments/assets/61c8c54c-3c19-40db-a7e6-5e9a60837af9" />

<img width="1511" height="602" alt="P4 O s7" src="https://github.com/user-attachments/assets/8fcce0ec-6822-459b-a046-148f47556900" />

<img width="1452" height="651" alt="P4 O s8" src="https://github.com/user-attachments/assets/471d2f00-f71b-4134-9db1-b477afe8ac1b" />

---

## 5️⃣ Smart Home Digital Twin

Room-wise energy visualization.

<img width="1576" height="632" alt="P4 O s9" src="https://github.com/user-attachments/assets/d050c382-15ac-4431-b52e-37ff8b9b58c1" />

---

## 6️⃣ Energy Logs

Stores complete appliance energy history.

<img width="1535" height="772" alt="P4 O s10" src="https://github.com/user-attachments/assets/0317d04c-f30f-44ee-80d8-e9628d4bce5c" />

---

# 📈 Energy Calculations

## Power

```text
Power (W) = Voltage × Current
```

---

## Energy

```text
Energy (kWh) =
Power × Time / 1000
```

---

## Cost Estimation

```text
Cost = Energy × Tariff Rate
```

---

## Carbon Emission

```text
CO₂ = Energy × 0.82
```

---


# 📦 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Home-Energy-Monitoring-System.git
```

Move Into Project

```bash
cd Smart-Home-Energy-Monitoring-System
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Initialize Database

```bash
python database/init_db.py
```

---

## Start Energy Simulation

```bash
python simulator/data_generator.py
```

---

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📉 Sample Output

```text
Voltage : 230V

Current : 5.8A

Power : 1334W

Energy : 1.33 kWh

Cost : ₹11.34

Status : ON
```

---

# 💡 Smart Recommendations

The system automatically identifies:

- Highest Energy Consumer
- Potential Energy Savings
- Peak Usage Hours
- Appliance Optimization Suggestions

Example:

```text
Highest Consumer: Air Conditioner

Potential Saving: 320W

Recommendation:
Reduce runtime by 15%.
Use eco mode during peak hours.
```

---

# 🌍 Industry Relevance

Similar systems are used by:

### Smart Homes

Monitor appliance energy usage.

### Commercial Buildings

Reduce electricity expenses.

### Factories

Track machine energy consumption.

### Energy Companies

Analyze customer load patterns.

### Smart Cities

Optimize energy distribution.

---

# 📋 Future Enhancements

- MQTT Integration
- ESP32 Hardware Integration
- Home Assistant Integration
- Grafana Dashboard
- AI Energy Forecasting
- Solar Energy Analytics
- Mobile Application
- Smart Automation Rules

---

# 🎓 Learning Outcomes

This project demonstrates:

- IoT System Design
- Energy Analytics
- Dashboard Development
- Database Management
- Data Visualization
- Smart Home Technologies
- Industry-Level Monitoring Systems

---

# 👨‍💻 Author

**Shweta Singh**

B.Tech Electronics & Computer Engineering

IoT | AI | Data Analytics | Embedded Systems

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---

## Thank You

**Smart Home Energy Monitoring System**
Building Smarter, Greener, and More Efficient Homes Through Data.
