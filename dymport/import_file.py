"""
Various functions to dynamically import (abitrary names from) arbitrary files.

To import a file like it is a module, use `import_file`.
"""

from sys import version_info


def import_file(name, file):
    """
    Import `file` as a module with _name_.

    Raises an ImportError if it could not be imported.
    """
    if version_info >= (3, 5):
        from importlib.util import module_from_spec, spec_from_file_location

        spec = spec_from_file_location(name, file)

        if not spec:
            raise ImportError("Could not import: '{}'".format(file))

        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    elif version_info >= (3, 3):
        from importlib.machinery import SourceFileLoader

        try:
            module = SourceFileLoader(name, file).load_module()
        except FileNotFoundError:
            raise ImportError("Could not import: '{}'".format(file))

        return module

    else:
        raise ImportError("Dymport: unsupported Python version, could not "
                          "import '{}'".format(file))
