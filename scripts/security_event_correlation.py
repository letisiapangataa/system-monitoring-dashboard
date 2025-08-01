import re
import time
from collections import deque

# Example log file path (update as needed)
LOG_FILE = '/var/log/auth.log'
CPU_THRESHOLD = 85
LOGIN_FAIL_PATTERN = re.compile(r'Failed password')

# Store recent events for correlation
recent_events = deque(maxlen=100)

def parse_log_line(line):
    if LOGIN_FAIL_PATTERN.search(line):
        return 'login_failure'
    return None

def correlate_events(cpu_usage, events):
    # Example: flag if high CPU and multiple login failures in short period
    login_fails = sum(1 for e in events if e == 'login_failure')
    if cpu_usage > CPU_THRESHOLD and login_fails >= 3:
        print(f"[ALERT] High CPU ({cpu_usage}%) and {login_fails} login failures detected!")

if __name__ == '__main__':
    import psutil
    print('Starting security event correlation. Press Ctrl+C to stop.')
    try:
        with open(LOG_FILE, 'r') as f:
            # Seek to end of file
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(2)
                    continue
                event = parse_log_line(line)
                if event:
                    recent_events.append(event)
                cpu = psutil.cpu_percent()
                correlate_events(cpu, recent_events)
    except KeyboardInterrupt:
        print('\nCorrelation stopped.')
    except FileNotFoundError:
        print(f'Log file {LOG_FILE} not found. Update LOG_FILE path.')
