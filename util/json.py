import json


def read(tofile):
    from os.path import isfile

    if isfile(tofile):
        with open(tofile) as data_file:
            return json.load(data_file)


def write(content, tofile):
    with open(tofile, 'w+') as data_file:
        json.dump(content, data_file, indent=4)