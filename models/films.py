from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_films = []

_engine = create_engine('sqlite:////tmp/teste.db', echo=True)
_Base = declarative_base(bind=_engine)


class Film(base=_Base):
    __tablename__ = 'films'
    path = Column(Unicode(40), primary_key=True, nullable=False)
    watched = Column(Boolean, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, path, date_created, watched=False):
        self.path = path
        self.watched = watched
        self.date_created = date_created


def get_session(base=_Base, engine=_engine):
    _Base.metadata.create_all()
    session = sessionmaker(bind=engine)
    return session()


def load(base=_Base, engine=_engine):
    session = get_session()
    for film in session.query(Film):
        print(type(film), film.path, film.watched, film.date_created)


def save(base=_Base, engine=_engine):
    session = get_session()

    f = Film('', 'datetest')
    f.watched = True

    session.add_all([f])
    session.commit()


def find_films(directories, extensions=[], minimum=0):
    from os import walk
    from os.path import join

    for directory in directories:
        for root, dirnames, filenames in walk(directory):
            for filename in filenames:
                absolute_path = join(root,filename)
                if filename.lower().endswith(tuple(extensions)) and os.stat(absolute_path).st_size > minimum:
                    _films.append(absolute_path)
                    #todo Scope for films[]

    sorted(_films)

#todo Add film or films
#todo Save to SQLite