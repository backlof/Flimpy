import os
import sys


def run(path):
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