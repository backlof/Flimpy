# Organization: make modules reusable

from models.settings import Settings
from models.library import Library


def prompt_dir():
    from tkinter import filedialog
    filedialog.Tk().withdraw()
    directory = filedialog.askdirectory()
    return directory


def main():
    #settings = Settings()
    lib = Library()
    lib.update()

    #settings.save()

    lib.save()


if __name__ == '__main__':
    main()