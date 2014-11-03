from models.library import Library


def prompt_dir():
    from tkinter import filedialog
    filedialog.Tk().withdraw()
    directory = filedialog.askdirectory()
    return directory


def main():
    lib = Library()
    lib.update()
    lib.save()


if __name__ == '__main__':
    main()