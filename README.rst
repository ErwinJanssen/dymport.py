Dynamic import
==============

Sometimes you want to import some Python file by it's path only. This might
be a dynamically generated path, placing a __init__ in the directory might
not be an option. Maybe you are building some kind of plugin system, or want
to inject a dependency?

Dymport got you covered, it provides several function to import a file by path,
or import specific names from that file. It works on all major Python version,
providing a uniform interface for dynamically import arbitrary Python files.
