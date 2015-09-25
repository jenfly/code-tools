"""Handy utilities for .py files."""


def _function_name(line):
    """Return the name of function defined in line."""
    if not line.startswith('def '):
        return None

    name = line.split('def ')[1]
    name = name.split('(')[0]
    return name

def function_list(filename):
    """Return and display a list of functions from a .py file."""

    # Extract all function names
    with open(filename, 'rU') as f:
        names = []
        for line in f:
            name = _function_name(line)
            if name is not None:
                names.append(name)

    # Print the names to the screen, with indents and comma separated
    pad = '    '
    for name in names:
        print(pad + name + ',')

    return names
