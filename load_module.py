from importlib import import_module
import sys


def load_module(name, exit_on_error=True, out=sys.stderr):
    """
    Load the module with the given name from the Modules directory.

    :param name:
        The name of the module, this function looks in the directory `Modules`
        for a file with the name <name>.py containing the class with the same
        <name>. The return value is this class.

    :param exit_on_error:
        If exit_on_error is True and a file or class with <name> cannot be
        found, an error message is printed and sys.exit is called. Other
        exceptions will not be caught.
        If exit_on_error is False, no exceptions will be caught. If a file with
        <name> cannot be found in the `Modules` directory, an
        `ImportError` will be raised. If the file is found, but doesn't
        contain a class called <name>, an `AttributeError` will be raised.

    :param out:
        The stream where the error messages will be writen to if an error
        occurs and `exit_on_error` is True.
    """
    try:
        return getattr(import_module('Modules.' + name), name)
    except (AttributeError, ImportError) as e:
        if not exit_on_error:
            raise e
        else:
            print("The module '%s' could not be found." % name, file=out)
            sys.exit(1)
