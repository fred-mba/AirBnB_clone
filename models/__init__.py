#!/usr/bin/python3
"""- Creates a unique FileStorage instance for the application
   - Allows all modules to access same storage instance, ensuring consistency
     in object storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
