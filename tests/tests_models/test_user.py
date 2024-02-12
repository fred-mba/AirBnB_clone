#!/usr/bin/python3
"""Test the User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User details"""
    def setUp(self):
        """Imports User class methods for all test cases"""
        self.user = User()

    def test_var_initialization(self):
        """Testing for attributes initializations"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_var_values(self):
        """Testing default values of all attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_instance(self):
        """Tests an instance type of the attribute"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == "__main__":
    unittest.main()
