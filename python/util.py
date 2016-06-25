import os
import functools

# Current directory
# If you call this from the current directory without abspath,
# then it will not work since __file__ is a relative path
os.path.dirname(os.path.abspath(__file__))

def all_sub_files(root):
    """Get all files in a directory.

    Never use os.walk again
    """
    for path, subdirs, files in os.walk(root):
        for name in files:
            yield os.path.join(path, name)


def lmap(*args, **kwargs):
    """Take map generator and make a list for Python 3 work"""
    return list(map(*args, **kwargs))


def lfilter(*args, **kwargs):
    """Take filter generator and make a list for Python 3 work"""
    return list(filter(*args, **kwargs))


def lreduce(*args, **kwargs):
    """Take reduce generator and make a list for Python 3 work"""
    return list(functools.reduce(*args, **kwargs))


def lzip(*args, **kwargs):
    """Take zip generator and make a list for Python 3 work"""
    return list(zip(*args, **kwargs))
