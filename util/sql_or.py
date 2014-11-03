from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class SQL():
    def __init__(self, filename='library'):
        self.filename = filename
        self._engine = create_engine('sqlite:///' + filename + '.db', echo=True)
        self._Base = declarative_base(bind=self._engine)
        self._Base.metadata.create_all()
        self.session = sessionmaker(bind=self._engine)

    def query(self, myclass):
        return self.session.query(myclass)

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()

    def add_all(self, objects):
        self.session.add_all(objects)
        self.session.commit()

    def __del__(self):
        self.session.close_all()