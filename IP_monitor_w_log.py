import requests
import time
import os
from datetime import datetime

def get_external_ip():
    """Fetch the current external IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

def log_ip_change(log_file, old_ip, new_ip):
    """Log the IP change to a file."""
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - IP changed from {old_ip} to {new_ip}\n"
        file.write(log_entry)
        print(log_entry.strip())

def monitor_ip(interval=60):
    """
    Monitor the external IP address for changes and log them.

    Args:
        interval (int): Time in seconds between checks.
    """
    # Determine the log file location on Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    log_file = os.path.join(desktop_path, "ip_monitor_log.txt")

    print(f"Starting public IP monitor. Log file: {log_file}")
    current_ip = get_external_ip()

    if current_ip:
        print(f"Initial IP address: {current_ip}")
    else:
        print("Could not fetch initial IP. Exiting.")
        return

    while True:
        time.sleep(interval)
        new_ip = get_external_ip()

        if new_ip:
            if new_ip != current_ip:
                print(f"Public IP has changed! Old IP: {current_ip}, New IP: {new_ip}")
                log_ip_change(log_file, current_ip, new_ip)
                current_ip = new_ip
            else:
                print(f"No change in IP. Current IP: {current_ip}")
        else:
            print("Failed to fetch IP. Retrying...")

if __name__ == "__main__":
    # Set the interval (in seconds) for checking the IP
    CHECK_INTERVAL = 60  # Change this value as needed
    monitor_ip(CHECK_INTERVAL)
