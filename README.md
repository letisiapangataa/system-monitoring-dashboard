# 💻 System Monitoring Dashboard (ALP)

A system monitoring and alerting solution built to track infrastructure health, performance metrics, and security events in real-time. This lab demonstrates full-stack observability using Python, Prometheus, InfluxDB, and Grafana.

For a lab overview: https://letisiapangataa.github.io/posts/building-a-system-monitoring-dashboard/

---

## Project Overview

This project simulates a real-world infrastructure observability stack tailored for system engineers and administrators. It includes real-time monitoring, historical analysis, alerting workflows, and security event correlation.

---

## Key Highlights

- **Real-Time Performance Monitoring**: Tracks CPU, memory, disk, and network usage.
- **Custom Alerting Workflows**: Sends notifications based on thresholds for performance or security anomalies.
- **Historical Data Analysis**: Stores time-series data for long-term performance insights.
- **Security Event Correlation**: Analyzes log patterns and correlates with system behavior to detect suspicious activity.

---

## Technologies Used

| Technology     | Purpose                                    |
|----------------|--------------------------------------------|
| Python         | Custom metrics collection and alert scripts|
| Prometheus     | Metrics scraping and time-series database  |
| InfluxDB       | Historical data storage                    |
| Grafana        | Visual dashboards and alerting UI          |

---

## Repository Structure

| Folder        | Contents                                         |
|---------------|--------------------------------------------------|
| `/dashboards/`| JSON files for Grafana dashboards                |
| `/configs/`   | Configuration files for Prometheus, InfluxDB     |
| `/scripts/`   | Python scripts for exporting and alerting        |
| `/docs/`      | Setup guides and correlation reports             |

---

## Example Use Cases (Review)

- Prometheus scrapes metrics from system exporters and custom scripts.
- Grafana displays metrics on real-time dashboards.
- Python alerts via email/Slack when thresholds are crossed.
- InfluxDB stores historical performance data.
- Correlation logic flags high CPU + repeated login failures as suspicious.

---

## Getting Started: Running the System Metrics Exporter

1. **Install Python dependencies:**
   ```
   pip install psutil requests
   ```

2. **Start Prometheus Pushgateway** (default: http://localhost:9091)

3. **Run the exporter script:**
   ```
   python scripts/system_metrics_exporter.py
   ```
   The script will export system metrics every 15 seconds. Stop it anytime with `Ctrl+C`.

4. **Prometheus configuration:**
   Ensure your `configs/prometheus.yml` includes:
   ```yaml
   scrape_configs:
     - job_name: 'system_metrics'
       static_configs:
         - targets: ['localhost:9091']
   ```

---

## License

MIT License

---

## References

- [Grafana Documentation](https://grafana.com/docs/)
- [Prometheus Docs](https://prometheus.io/docs/)
- [InfluxDB Docs](https://docs.influxdata.com/)
- [Python psutil Module](https://pypi.org/project/psutil/)

---

## Disclaimer

This project was developed using a combination of publicly available learning resources, reference books, open source projects, and artificial intelligence tools. All efforts have been made to attribute and comply with relevant licenses. Contributions and insights from the broader open source and educational communities are gratefully acknowledged. This software is provided as-is, without warranty of any kind, express or implied. The author assumes no responsibility for any loss, damage, or disruption caused by the use of this code. It is intended for educational and experimental purposes only and may not be suitable for production environments.
