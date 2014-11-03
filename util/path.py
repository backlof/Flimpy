import os.path

#todo Test that this works
def same_drive(path, compare_to=None):
    if not compare_to:
        compare_to = current_dir()
    return len(os.path.commonprefix([path, compare_to])) > 2


def relative(directory, relative_from=None):
    if not relative_from:
        relative_from = current_dir()
    return os.path.relpath(directory, relative_from)


def absolute(path):
    return os.path.abspath(path)


def current_dir():
    path, script = os.path.split(os.path.realpath(__file__))
    return path


def remove_redundant(paths):
    if len(paths) < 2:
        return paths
    else:
        for path in paths:
            for x in paths:
                if x.startswith(path) and path != x:
                    paths.remove(x)
        return paths


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