#!/usr/bin/python3
"""Test the base class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Imports Base model methods for test cases"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_initialization(self):
        """Tests time and id generation"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

        self.assertIsInstance(self.base_model.id, str)

    def test_save_updates(self):
        """Testing update changes"""
        last_update_time = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(last_update_time, self.base_model.updated_at)

    def test_to_dict_output(self):
        """Testing if dictionary was succefully created"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_time_format(self):
        """Testing created_at and updated_at isoformat()"""
        obj_dict = self.base_model.to_dict()
        created_at = obj_dict['created_at']
        self.assertEqual(created_at, self.base_model.created_at.isoformat())
        updated_at = obj_dict['updated_at']
        self.assertEqual(updated_at, self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
