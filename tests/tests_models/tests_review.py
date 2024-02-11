#!/usr/bin/python3
"""Test the Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review scenarios"""
    def setUp(self):
        """Imports City class methods for all test cases"""
        self.review = Review()

    def test_var_initialization(self):
        """Testing for attributes initializations"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_var_values(self):
        """Testing default values of all attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_instance(self):
        """Tests an instance type of the attribute"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == "__main__":
    unittest.main()
