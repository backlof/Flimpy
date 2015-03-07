from models import library
from models.library import Library
import argparse
import sys


def prompt_dir():
    from tkinter import filedialog

    filedialog.Tk().withdraw()
    directory = filedialog.askdirectory()
    return directory


def prompt_yesno(question):
    valid = {"yes": True, "y": True, "no": False, "n": False}

    while True:
        result = input(question + " [y/n]: ").lower()
        if valid.__contains__(result):
            return valid[result]
        else:
            print("{} is not a valid choice".format(result))
            print("{}: {}".format("Please respond with one of the following",
                                  ", ".join(['%s' % (key) for (key, value) in valid.items()])))


#Make batch script for -add and -play modus
#Make shellscript for -add and -play modus
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Opens a random film you haven't seen before.")

    parser.add_argument(metavar='D', dest='directories', nargs='*', help='add directories to scan')

    config_group = parser.add_argument_group('application configurations')

    portable_group = config_group.add_mutually_exclusive_group()
    portable_group.add_argument('-a', '--absolute', dest='portable', action='store_false', help='use absolute paths')
    portable_group.add_argument('-p', '--portable', dest='portable', action='store_true', help='use relative paths')

    size_group = config_group.add_mutually_exclusive_group()
    size_group.add_argument('-mk', dest='minkb', action='store', type=int, help='set minimum size in kilobytes')
    size_group.add_argument('-mm', dest='minmb', action='store', type=int, help='set minimum size in megabytes')
    size_group.add_argument('-mg', dest='mingb', action='store', type=int, help='set minimum size in gigabytes')
    args = parser.parse_args()

    lib = Library()

    if len(sys.argv) > 1:
        if args.portable:
            lib.settings.portable_paths = args.portable
        if args.minkb:
            lib.settings.minimum_size_byte = args.minkb * 2^10
        elif args.minmb:
            lib.settings.minimum_size_byte = args.minmb * 2^20
        elif args.mingb:
            lib.settings.minimum_size_byte = args.mingb * 2^30
        if args.directories:
            print(args.directories)
            for directory in args.directories:
                print(directory)
                lib.settings.add_directory(directory)
    else:
        #lib.settings.add_directory(prompt_dir())
        lib.update()
        film = lib.random_movie()

        if film:
            print('Opening: {}'.format(film.path()))
            #film.watch()
            film.watched = prompt_yesno("Mark the film as watched?")

    lib.save()

    #if directory:
     #   lib.settings.add_directory(directory);