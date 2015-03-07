import os.path


def relative(directory, relative_from=None):
    if not relative_from:
        relative_from = current_dir()
    try:
        return os.path.relpath(directory, relative_from)
    except ValueError:
        return directory


def absolute(path):
    return os.path.abspath(path)


def exists(path):
    return os.path.exists(path)


def current_dir():
    path, script = os.path.split(os.path.realpath(__file__))
    return path


def join(path, *paths):
    return os.path.join(path, *paths)


def isabs(path):
    return os.path.isabs(path)


def run(path):
    import sys
    import os
    import subprocess

    # Windows
    if os.name == 'nt':
        os.startfile(path, 'open')
    # Mac OS X
    elif sys.platform.startswith('darwin'):
        subprocess.call(('open', path))
    # Linux
    elif os.name == 'posix':
        subprocess.call(('xdg-open', path))