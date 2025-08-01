import psutil
import time
from influxdb import InfluxDBClient

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'system_metrics'

client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT)
client.switch_database(INFLUXDB_DB)

def collect_metrics():
    return {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'net_sent': psutil.net_io_counters().bytes_sent,
        'net_recv': psutil.net_io_counters().bytes_recv
    }

def format_influxdb(metrics):
    return [{
        'measurement': 'system_metrics',
        'fields': metrics
    }]

if __name__ == '__main__':
    print('Starting InfluxDB exporter. Press Ctrl+C to stop.')
    try:
        while True:
            metrics = collect_metrics()
            data = format_influxdb(metrics)
            try:
                client.write_points(data)
            except Exception as e:
                print(f'Failed to write to InfluxDB: {e}')
            time.sleep(15)
    except KeyboardInterrupt:
        print('\nExporter stopped.')
