from models.library import Library
import argparse
import math


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
    portable_group.add_argument('-p', '--portable', dest='portable', action='store_true', default=False, help='use relative paths')
    portable_group.add_argument('-a', '--absolute', dest='absolute', action='store_true', default=False, help='use absolute paths')

    size_group = config_group.add_mutually_exclusive_group()
    size_group.add_argument('-mk', dest='minkb', action='store', type=int, help='set minimum size in kilobytes')
    size_group.add_argument('-mm', dest='minmb', action='store', type=int, help='set minimum size in megabytes')
    size_group.add_argument('-mg', dest='mingb', action='store', type=int, help='set minimum size in gigabytes')
    args = parser.parse_args()
    print(args)

    lib = Library()

    if args.portable:
        lib.settings.portable_paths = True;
    if args.absolute:
        lib.settings.portable_paths = False;
    if args.minkb:
        lib.settings.minimum_size_byte = int(args.minkb * math.pow(2, 10))
    elif args.minmb:
        lib.settings.minimum_size_byte = int(args.minmb * math.pow(2, 20))
    elif args.mingb:
        lib.settings.minimum_size_byte = int(args.mingb * math.pow(2, 30))
    if args.directories:
        #would lose all watched films if forgot one dir
        #maybe only add is a good idea?
        lib.settings.abspath_directories = []
        lib.settings.relpath_directories = []

        for directory in args.directories:
            lib.settings.add_directory(directory)

    #lib.settings.add_directory(prompt_dir())
    lib.update()
    film = lib.random_movie()

    if film:
        print('Opening: {}'.format(film.path()))
        #film.watch()
        film.watched = prompt_yesno("Mark the film as watched?")

    lib.save()