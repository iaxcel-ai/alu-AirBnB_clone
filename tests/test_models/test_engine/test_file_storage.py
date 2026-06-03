#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorageDocstrings(unittest.TestCase):
    """Tests for FileStorage docstrings."""

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.engine.file_storage as fs_module
        self.assertIsNotNone(fs_module.__doc__)

    def test_class_docstring(self):
        """Test that FileStorage class has a docstring."""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all_docstring(self):
        """Test that all method has a docstring."""
        self.assertIsNotNone(FileStorage.all.__doc__)

    def test_new_docstring(self):
        """Test that new method has a docstring."""
        self.assertIsNotNone(FileStorage.new.__doc__)

    def test_save_docstring(self):
        """Test that save method has a docstring."""
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_reload_docstring(self):
        """Test that reload method has a docstring."""
        self.assertIsNotNone(FileStorage.reload.__doc__)


class TestFileStorageAttributes(unittest.TestCase):
    """Tests for FileStorage private class attributes."""

    def test_file_path_is_private(self):
        """Test that __file_path is a private class attribute."""
        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_file_path_is_string(self):
        """Test that __file_path is a string."""
        self.assertIsInstance(
            FileStorage._FileStorage__file_path, str)

    def test_objects_is_private(self):
        """Test that __objects is a private class attribute."""
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_objects_is_dict(self):
        """Test that __objects is a dictionary."""
        self.assertIsInstance(
            FileStorage._FileStorage__objects, dict)


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_file_storage_instantiation(self):
        """Test that FileStorage instantiates correctly."""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_storage_is_file_storage(self):
        """Test that storage is an instance of FileStorage."""
        self.assertIsInstance(storage, FileStorage)


class TestFileStorageAll(unittest.TestCase):
    """Tests for FileStorage all method."""

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_returns_same_dict(self):
        """Test that all returns the same dict object each call."""
        self.assertIs(storage.all(), storage.all())


class TestFileStorageNew(unittest.TestCase):
    """Tests for FileStorage new method."""

    def test_new_adds_to_objects(self):
        """Test that new adds an object to __objects."""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except Exception:
            pass


class TestFileStorageSave(unittest.TestCase):
    """Tests for FileStorage save method."""

    def test_save_creates_file(self):
        """Test that save creates the JSON file."""
        obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_contains_object(self):
        """Test that the saved file contains the object."""
        obj = BaseModel()
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, data)

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except Exception:
            pass


class TestFileStorageReload(unittest.TestCase):
    """Tests for FileStorage reload method."""

    def test_reload_loads_objects(self):
        """Test that reload loads objects from the file."""
        obj = BaseModel()
        obj.save()
        storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_reload_no_file_no_error(self):
        """Test that reload raises no error if file doesn't exist."""
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload raised exception: {}".format(e))

    def test_reload_returns_none(self):
        """Test that reload returns None."""
        self.assertIsNone(storage.reload())

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
