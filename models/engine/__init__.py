#!/usr/bin/python3
# models/__init__.py
from os import getenv

# Determine the type of storage to use
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()
