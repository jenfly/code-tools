#!/usr/bin/python

"""Handy utilities for .py files.

Import as a module in Python or run as a command line script.
"""

import sys

def funclist(filename):
    """Return and display a list of functions from a .py file."""

    def function_name(line):
        """Return the name of function defined in line."""
        if not line.startswith('def '):
            return None

        name = line.split('def ')[1]
        name = name.split('(')[0]
        return name

    # Extract all function names
    with open(filename, 'rU') as f:
        names = []
        for line in f:
            name = function_name(line)
            if name is not None:
                names.append(name)

    # Print the names to the screen, with indents and comma separated
    pad = '    '
    for name in names:
        print(pad + name + ',')

    return names

def main():
    args = sys.argv[1:]
    if not args:
        raise RuntimeError('Usage: code_tools funcname [args]')

    # Get function name from first command line argument and call function
    # with remaining arguments as input
    funcname = args.pop(0)
    if funcname not in globals().keys():
        raise RuntimeError('Function ' + funcname + ' not found.')
    func = globals()[funcname]
    func(*args)


if __name__ == "__main__":
    main()
