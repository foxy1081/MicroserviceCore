# test_microservicecore.py
"""
Tests for MicroserviceCore module.
"""

import unittest
from microservicecore import MicroserviceCore

class TestMicroserviceCore(unittest.TestCase):
    """Test cases for MicroserviceCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MicroserviceCore()
        self.assertIsInstance(instance, MicroserviceCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MicroserviceCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
