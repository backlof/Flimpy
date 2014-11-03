from sqlalchemy import Column, Unicode, Boolean, DateTime, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from util import path
from models.settings import Settings

_filename = 'library' + '.db'
_engine = create_engine('sqlite:///' + _filename, echo=True)
Base = declarative_base(bind=_engine)
Session = sessionmaker(bind=_engine)
session = Session()


class Film(Base):
    __tablename__ = 'films'
    file = Column(Unicode(120), primary_key=True, nullable=False)
    watched = Column(Boolean, nullable=False)
    date_created = Column(DateTime(timezone=True), nullable=False)
    size = Column(Integer, nullable=False)

    def __init__(self, file, date_created, size, watched=False):
        self.file = file
        self.watched = watched
        self.date_created = date_created
        self.size = size

    def __eq__(self, other):
        return self.file == other.file

    def save(self):
        session.add(self)
        session.commit()

    def print(self):
        print(type(self), self.file, self.watched, self.date_created)

# Has to be after model class
Base.metadata.create_all()


class Library():
    def __init__(self):
        self.films = []
        self.films = session.query(Film).all()
        self.settings = Settings()

    def save(self):
        session.add_all(self.films)
        session.commit()

        self.settings.save()

    def update(self):
        from os import walk

        found = []

        for directory in self.settings.directories:
            for root, dirnames, filenames in walk(directory):
                for filename in filenames:
                    absolute = os.path.join(root, filename)
                    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(absolute)
                    if filename.lower().endswith(tuple(self.settings.file_extensions)):
                        if size > self.settings.minimum_size_byte:
                            found.append(Film(file=absolute, date_created=get_datetime(ctime), size=size))

        # Film has been removed from disk - remove from database
        for film in self.films:
            #film.print()
            if film not in found:
                del film

        # Film has been added to disk - add to database
        for film in found:
            #print('Found: ' + film.file)
            if film not in self.films:
                self.films.append(film)


def get_datetime(timestamp):
    from datetime import datetime
    return datetime.fromtimestamp(timestamp)