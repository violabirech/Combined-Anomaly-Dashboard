# Unified DNS + DoS Anomaly Detection Dashboard

A modular Streamlit dashboard for real-time and historical anomaly detection in network traffic (DNS + DoS) using ML models via Hugging Face APIs and InfluxDB.

## 🚀 Features
- Dynamic tab navigation: Overview, Live Stream, Manual Entry, Metrics, and Historical Data
- Real-time data from InfluxDB
- ML inference through Hugging Face Space API
- Discord alert and anomaly highlighting
- Ready for Docker and Hugging Face deployment

## 🐳 Docker Usage
```bash
docker build -t anomaly-dashboard .
docker run -p 8501:8501 anomaly-dashboard
```

Or using docker-compose:
```bash
docker-compose up
```

## 🤖 API
- DNS: `https://violabirech-dos-anomalies-detection.hf.space/predict/dns`
- DoS: `https://violabirech-dos-anomalies-detection.hf.space/predict/dos`

## 📂 Structure
```
app.py
tabs/
  ├── overview_tab.py
  ├── metrics_tab.py
  ├── live_stream_tab.py
  ├── manual_entry_tab.py
  └── historical_tab.py
```
