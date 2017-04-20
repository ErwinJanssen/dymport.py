"""
Various functions to dynamically import (abitrary names from) arbitrary files.

To import a file like it is a module, use `import_file`.
"""

from importlib.util import module_from_spec, spec_from_file_location


def import_file(name, file):
    """
    Import `file` as a module with _name_.

    Raises an ImportError if it could not be imported.
    """
    spec = spec_from_file_location(name, file)

    if not spec:
        raise ImportError("Could not import: '{}'".format(file))

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
