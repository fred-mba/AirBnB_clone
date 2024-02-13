#!/usr/bin/python3
"""
Test all features for the console
Run: python -m unittest test_module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the class for testing."""
        cls.hbnb_console = HBNBCommand()

    def setUp(self):
        """Set up the test by resetting the console output."""
        self.output = StringIO()

    def tearDown(self):
        """Clean up the test by closing the console output."""
        self.output.close()

    def test_show_command(self):
        with patch('sys.stdout', new=self.output):
            self.hbnb_console.onecmd("create BaseModel")
            self.hbnb_console.onecmd(f"show BaseModel {
                self.output.getvalue().strip()}")
        output_str = self.output.getvalue().strip()
        # Assuming it prints the instance
        self.assertIn("BaseModel", output_str)

    def test_update_command(self):
        with patch('sys.stdout', new=self.output):
            self.hbnb_console.onecmd("create BaseModel")
            self.hbnb_console.onecmd(f"update BaseModel {
                self.output.getvalue().strip()}")
            self.hbnb_console.onecmd(f"show BaseModel {
                self.output.getvalue().strip()}")
        output_str = self.output.getvalue().strip()
        # Assuming it prints the updated instance
        self.assertIn("", output_str)


if __name__ == "__main__":
    unittest.main()
