import psutil
import requests
import socket

class SystemMonitor:
    def __init__(self):
        pass

    def check_disk_usage(self, threshold=20):
        # Get disk usage statistics
        disk_usage = psutil.disk_usage('/')
        # Check if disk usage is below the threshold
        return disk_usage.percent < threshold
    
    def check_cpu_utilization(self, threshold=75):
        # Get the CPU usage percentage
        cpu_usage = psutil.cpu_percent(1)
        # Check if CPU usage is below the threshold
        return cpu_usage < threshold
    
    def check_localhost(self):
        try:
            # Try to bind to the localhost to check if it's up and running
            sock = socket.create_connection(("localhost"), 80)
            sock.close()
            return True
        except socket.error:
            return False
        
    def check_internet_connectivity(self, url='http://www.google.com'):
        try:
            # Send a GET request to the specified URL
            response = requests.get(url)
            # Check if the response status code is OK
            return response.status_code == 200
        except requests.RequestException:
            return False
        
    def run_checks(self):
        # Run all the checks and print the results
        if not self.check_disk_usage():
            print("ERROR! Disk usage is above the set threshold.")
        elif not self.check_cpu_utilization():
            print("ERROR! CPU utilization is above the set threshold.")
        elif not self.check_localhost():
            print("ERROR! Localhost is not available.")
        elif not self.check_internet_connectivity():
            print("ERROR! Unable to connect to the internet.")
        else:
            print("Everything is ok!")

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.run_checks()
