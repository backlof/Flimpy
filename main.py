# Organization: make modules reusable

from models.settings import *


def main():
    settings = Settings()
    settings.load()
    settings.save()


if __name__ == '__main__':
    main()