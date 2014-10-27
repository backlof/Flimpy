# Organization: make modules reusable

from models.settings import *


def main():
    settings = Settings()
    settings.load()

    from tkinter import filedialog
    filedialog.Tk().withdraw()

    settings.add_directory(filedialog.askdirectory())
    print(settings.directories)
    settings.save()


if __name__ == '__main__':
    main()