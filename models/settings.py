from util import json
from util import path

_filename = 'settings' + '.json'


# Contains user settings for application
class Settings:
    def __init__(self, abspath_directories=[], relpath_directories=[],
                 file_extensions=['.mkv', 'avi', '.flv', '.mov', '.wmv', '.mpg', '.mpeg', '.m4v', 'mp4'],
                 minimum_size_byte=52428800, portable_paths=False):
        self.abspath_directories = abspath_directories
        self.relpath_directories = relpath_directories
        self.file_extensions = file_extensions
        self.minimum_size_byte = minimum_size_byte
        self.portable_paths = portable_paths
        self.load()

    # Load attributes from JSON
    def load(self):
        dictionary = json.read(_filename)

        if dictionary:
            for key in dictionary:
                setattr(self, key, dictionary[key])

            self.file_extensions = sorted(self.file_extensions)

    def save(self):
        json.write(self, _filename)

    def directories(self):
        return self.relpath_directories if self.portable_paths else self.abspath_directories

    def remove_directory(self, directory):
        index = self.directories().index(directory)
        del self.relpath_directories[index]
        del self.abspath_directories[index]

    def add_directory(self, directory):
        if path.exists(directory):
            absolute = path.absolute(directory)
            relative = path.relative(directory)

            if self.directories().__contains__(relative) or self.directories().__contains__(absolute):
                print("The directory is already added.")
            else:
                self.relpath_directories.append(relative)
                self.abspath_directories.append(absolute)

            # Remove subfolders to avoid duplicates
            for x in self.directories():
                for y in self.directories():
                    if x != y and y.startswith(x):
                        if path.isabs(y):
                            # Delete the longest
                            self.remove_directory(y)
                        else:
                            # Delete the shortest
                            self.remove_directory(x)
        else:
            print("The directory doesn't exist.")