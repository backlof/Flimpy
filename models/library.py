from models.settings import Settings
from util import json
from util import path
from os import stat


_filename = 'films' + '.json'
portable_paths = False


class Film():
    def __init__(self, abspath, last_modification, size, relpath=None, watched=False):
        self.abspath = abspath
        self.relpath = relpath if relpath else path.relative(abspath)
        self.watched = watched
        self.last_modification = last_modification
        self.size = size

    def path(self):
        return self.abspath if portable_paths else self.relpath

    def __eq__(self, other):
        return self.path() == other.path()

    def print(self):
        print(type(self), self.path())

    def watch(self):
        path.run(self.path())


class Library():
    def __init__(self):
        self.films = []
        self.settings = Settings()
        global portable_paths
        portable_paths = self.settings.portable_paths
        self._load()

    def _load(self):
        content = json.read(_filename)
        if content:
            for dictionary in content:
                self.films.append(Film(**dictionary))

    def save(self):
        json.write(self.films, _filename)
        self.settings.save()

    def update(self):
        from os import walk

        found = []

        for directory in self.settings.directories():
            if path.exists(directory):
                for root, dirnames, filenames in walk(directory):
                    for filename in filenames:

                        # Get around the 256 character limit by prepending \\\\?\\
                        absolute = path.join("\\\?\\", root, filename)

                        if filename.lower().endswith(tuple(self.settings.file_extensions)):

                            mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = stat(absolute)
                            if size > self.settings.minimum_size_byte:

                                found.append(Film(abspath=absolute, last_modification=get_datetime(mtime), size=size))
            else:
                self.settings.directories().remove(directory)

        # Film has been removed from disk - remove from library
        for film in self.films:
            if film not in found:
                #print('Removed: {}'.format(film.print()))
                self.films.remove(film)
                #del film

        # New film - add to library
        for film in found:
            if film not in self.films:
                #print('Found: {}'.format(film.print()))
                self.films.append(film)

    def random_movie(self):
        import random

        if self.films:
            found = []

            for film in self.films:
                if not film.watched:
                    found.append(film)

            if found:
                return random.choice(found)
            else:
                print("There are no unwatched films.")
                return None
        else:
            print("There are no films added.")
            return None


def get_datetime(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(timestamp)