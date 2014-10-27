from util import json
from util.path import *

_filename = 'settings' + '.json'
#todo Use <sorted(list)> to remove duplicatess


# Contains user settings for application
class Settings:
    def __init__(self, directories=[], file_extensions=['.mkv'], exclude=[], minimum_size_byte=0, portable=False):
        self.directories = directories
        self.file_extensions = file_extensions
        self.exclude = exclude
        self.minimum_size_byte = minimum_size_byte
        self.portable = portable

    # Load attributes from JSON
    def load(self):
        dictionary = json.read(_filename)

        if dictionary:
            for key in dictionary:
                setattr(self, key, dictionary[key])

            self.directories = remove_redundant(self.directories)
            self.file_extensions = sorted(self.file_extensions)
            self.exclude = sorted(self.exclude)

    # Convert class attributes to a dictionary
    def to_dictionary(self):
        return self.__dict__

    # Save class attributes to file in JSON format
    # Uses dictionary conversion instead of JSON serialization
    def save(self):
        json.write(self.to_dictionary(), _filename)

    def add_directory(self, path):
        self.directories.append(path)
        self.directories = remove_redundant(self.directories)
