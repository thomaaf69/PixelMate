# test_pixelmate.py
"""
Tests for PixelMate module.
"""

import unittest
from pixelmate import PixelMate

class TestPixelMate(unittest.TestCase):
    """Test cases for PixelMate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelMate()
        self.assertIsInstance(instance, PixelMate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelMate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
