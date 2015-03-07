import json


def read(tofile):
    from os.path import isfile

    if isfile(tofile):
        with open(tofile) as data_file:
            return json.load(data_file)


def write(content, tofile):
    with open(tofile, 'w+') as data_file:
        json.dump(content, data_file, default=json_serialize, indent=4)


def json_serialize(obj):
    from datetime import datetime
    import models.library
    import models.settings

    if isinstance(obj, datetime):
        return obj.isoformat()

    if isinstance(obj, models.library.Film):
        return obj.__dict__

    if isinstance(obj, models.settings.Settings):
        return obj.__dict__

    return obj