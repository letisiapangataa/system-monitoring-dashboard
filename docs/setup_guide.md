# System Monitoring Dashboard - Setup Guide

## Prerequisites
- Python 3.x
- Prometheus
- InfluxDB
- Grafana
- Prometheus Pushgateway
- Python packages: psutil, requests, influxdb

## 1. Install Python dependencies
```
pip install psutil requests influxdb
```

## 2. Configure Prometheus
- Use the provided `configs/prometheus.yml`.
- Start Prometheus and Pushgateway.

## 3. Configure InfluxDB
- Use the provided `configs/influxdb.conf`.
- Create a database named `system_metrics` in InfluxDB.

## 4. Run Exporters
- For Prometheus:
  ```
  python scripts/system_metrics_exporter.py
  ```
- For InfluxDB:
  ```
  python scripts/influxdb_exporter.py
  ```

## 5. Run Alerting
```
python scripts/alerting.py
```

## 6. Run Security Event Correlation
- Update the log file path in `security_event_correlation.py` if needed.
```
python scripts/security_event_correlation.py
```

## 7. Import Grafana Dashboard
- Use `dashboards/grafana-dashboard.json` in Grafana.

---

For more details, see the README.md.
