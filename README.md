# 📊 System Monitoring Dashboard

A custom system monitoring and alerting solution built to track infrastructure health, performance metrics, and security events in real-time. This lab demonstrates full-stack observability using Python, Prometheus, InfluxDB, and Grafana.

---

## 📌 Project Overview

This project simulates a real-world infrastructure observability stack tailored for system engineers and administrators. It includes real-time monitoring, historical analysis, alerting workflows, and security event correlation.

---

## 🛠️ Key Highlights

- ⚙️ **Real-Time Performance Monitoring**: Tracks CPU, memory, disk, and network usage.
- 🚨 **Custom Alerting Workflows**: Sends notifications based on thresholds for performance or security anomalies.
- 📈 **Historical Data Analysis**: Stores time-series data for long-term performance insights.
- 🛡️ **Security Event Correlation**: Analyzes log patterns and correlates with system behavior to detect suspicious activity.

---

## 🔧 Technologies Used

| Technology     | Purpose                                    |
|----------------|--------------------------------------------|
| Python         | Custom metrics collection and alert scripts|
| Prometheus     | Metrics scraping and time-series database  |
| InfluxDB       | Historical data storage                    |
| Grafana        | Visual dashboards and alerting UI          |

---

## 📂 Repository Structure

| Folder        | Contents                                         |
|---------------|--------------------------------------------------|
| `/dashboards/`| JSON files for Grafana dashboards                |
| `/configs/`   | Configuration files for Prometheus, InfluxDB     |
| `/scripts/`   | Python scripts for exporting and alerting        |
| `/docs/`      | Setup guides and correlation reports             |

---

## 🧪 Example Use Case

- Prometheus scrapes metrics from system exporters and custom scripts.
- Grafana displays metrics on real-time dashboards.
- Python alerts via email/Slack when thresholds are crossed.
- InfluxDB stores historical performance data.
- Correlation logic flags high CPU + repeated login failures as suspicious.

---

## 📷 Dashboard Preview

![Grafana Dashboard](dashboards/grafana-dashboard.png)

---

## 📄 License

MIT License

---

## 📚 References

- [Grafana Documentation](https://grafana.com/docs/)
- [Prometheus Docs](https://prometheus.io/docs/)
- [InfluxDB Docs](https://docs.influxdata.com/)
- [Python psutil Module](https://pypi.org/project/psutil/)
