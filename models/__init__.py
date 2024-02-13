#!/usr/bin/python3
"""
Initialization for models with unique storage and calling reload
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
