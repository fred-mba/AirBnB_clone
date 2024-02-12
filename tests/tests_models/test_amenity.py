#!/usr/bin/python3
"""Test the Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test scenarios"""
    def setUp(self):
        """Initializes Amenity class for all test cases"""
        self.amenity = Amenity()

    def test_var_initialization(self):
        """Testing default value and name"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_attribute_instance(self):
        """Tests an isinstance type of the attribute"""
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
