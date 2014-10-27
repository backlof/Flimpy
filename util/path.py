from os.path import commonprefix
from os.path import abspath
from os.path import relpath
from os.path import split
from os.path import realpath


#todo Test that this works
def same_drive(path, compare_to=None):
    if not compare_to:
        compare_to = current_dir()
    return len(commonprefix([path, compare_to])) > 2


def absolute_path(path):
    return abspath(path)


def relative_path(directory, relative_from=None):
    if not relative_from:
        relative_from = current_dir()
    return relpath(directory, relative_from)


def current_dir():
    path, script = split(realpath(__file__))
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