from importlib.util import module_from_spec, spec_from_file_location
from sys import exit, stderr


def import_from_file(attribute, path_to_file):
    """
    Dynamically import a given attribute (class, function, etc.) from a file.

    :param attribute:
        The attribute to import. This can be a class, function, etc. If the
        attribute is not found in the specified file, an error is printed and
        exit() is called.

    :param path_to_file:
        The file from which to import the attribute. If the file does not exist,
        or can not be loaded for another reason, an error is printed and exit()
        is called.
    """
    spec = spec_from_file_location('import_from_file', path_to_file)

    if not spec:
        print('Error: Could not load the file "{}".'.format(path_to_file), file=stderr)
        exit(1)

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    try:
        return getattr(module, attribute)
    except AttributeError as e:
        print('Error: Attribute "{}" was not found in file "{}".'
              .format(attribute, path_to_file), file=stderr)
        exit(1)
