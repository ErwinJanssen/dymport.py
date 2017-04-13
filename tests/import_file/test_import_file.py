from dymport import import_file

from os import path
from unittest import TestCase


here = path.abspath(path.dirname(__file__))


class TestImportFile(TestCase):

    def test_non_existing_file(self):
        with self.assertRaises(ImportError):
            import_file('name', 'invalid')

    def test_non_python_file(self):
        with self.assertRaises(ImportError):
            import_file('name', path.join(here, 'file.txt'))

    def test_valid_current_dir(self):
        module = import_file('current_dir', path.join(here, 'file.py'))

        self.assertEqual(module.TestClass.value, 'test_case')
        self.assertEqual(module.test_function(), 'success!')

    def test_valid_different_dir(self):
        module = import_file('subdir', path.join(here, 'subdir', 'subfile.py'))

        self.assertEqual(module.magic_numer, 42)
        self.assertEqual(module.some_function(), 'Hello from a different dir!')
