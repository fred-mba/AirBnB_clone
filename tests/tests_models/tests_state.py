#!/usr/bin/python3
"""Test the State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State test scenarios"""
    def setUp(self):
        """Initializes State class for all test cases"""
        self.state = State()

    def test_var_initialization(self):
        """Testing default value for name"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_attribute_instance(self):
        """Tests an isinstance type of the attribute"""
        self.assertIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
