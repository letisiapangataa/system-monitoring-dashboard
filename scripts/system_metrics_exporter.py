import psutil
import time
import requests

PROMETHEUS_PUSHGATEWAY = 'http://localhost:9091/metrics/job/system_metrics'

# Prometheus metric names should use snake_case and units where possible
METRIC_NAMES = {
    'cpu_usage': 'system_cpu_usage_percent',
    'memory_usage': 'system_memory_usage_percent',
    'disk_usage': 'system_disk_usage_percent',
    'net_sent': 'system_network_bytes_sent_total',
    'net_recv': 'system_network_bytes_recv_total'
}

# Collect system metrics
def collect_metrics():
    """Collect system metrics using psutil."""
    metrics = {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'net_sent': psutil.net_io_counters().bytes_sent,
        'net_recv': psutil.net_io_counters().bytes_recv
    }
    return metrics

def format_prometheus(metrics):
    """Format metrics in Prometheus exposition format."""
    lines = []
    for k, v in metrics.items():
        metric_name = METRIC_NAMES.get(k, k)
        lines.append(f"{metric_name} {v}")
    return '\n'.join(lines)

def push_metrics(metrics):
    """Push metrics to Prometheus Pushgateway with error handling."""
    data = format_prometheus(metrics)
    try:
        resp = requests.post(PROMETHEUS_PUSHGATEWAY, data=data)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to push metrics: {e}")

if __name__ == '__main__':
    print("Starting system metrics exporter. Press Ctrl+C to stop.")
    try:
        while True:
            metrics = collect_metrics()
            push_metrics(metrics)
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nExporter stopped.")
