import unittest
from system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        """Set up for the tests; create an instance of SystemMonitor"""
        self.monitor = SystemMonitor()

    def test_disk_usage(self):
        """Test the disk usage check."""
        self.assertTrue(self.monitor.check_disk_usage(), "Disk usage is above the threshold")

    def test_cpu_utilization(self):
        """Test the CPU utilization check."""
        self.assertTrue(self.monitor.check_cpu_utilization(), "CPU utilization is above the threshold")

    def test_localhost(self):
        """Test the CPU utilization check."""
        self.assertTrue(self.monitor.check_localhost(), "Localhost is not available")

    def test_internet_connectivity(self):
        """Test the CPU utilization check."""
        self.assertTrue(self.monitor.check_internet_connectivity(), "No internet connectivity")

if __name__ == '__main__':
    unittest.main()
