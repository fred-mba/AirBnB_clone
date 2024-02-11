#!/usr/bin/python3
"""Test the City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test scenarios"""
    def setUp(self):
        """Imports City class methods for all test cases"""
        self.city = City()

    def test_var_initialization(self):
        """Testing for name and state_id attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_var_values(self):
        """Testing default values of all attributes"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_attribute_instance(self):
        """Tests an instance type of the attribute"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)


if __name__ == "__main__":
    unittest.main()
