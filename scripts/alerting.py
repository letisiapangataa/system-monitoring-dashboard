import smtplib
import psutil
import time

ALERT_EMAIL = 'your@email.com'
THRESHOLDS = {
    'cpu': 90,
    'memory': 90
}

def send_email_alert(subject, body):
    # Placeholder: configure SMTP for your environment
    print(f'ALERT: {subject}\n{body}')

def check_alerts():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    if cpu > THRESHOLDS['cpu']:
        send_email_alert('High CPU Usage', f'CPU usage at {cpu}%')
    if mem > THRESHOLDS['memory']:
        send_email_alert('High Memory Usage', f'Memory usage at {mem}%')

if __name__ == '__main__':
    while True:
        check_alerts()
        time.sleep(30)
