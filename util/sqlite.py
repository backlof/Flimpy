import sqlite3

_filename = 'data' + '.db'


class DatabaseManager():
    def __init__(self, filename=_filename):
        self.connection = sqlite3.connect(_filename)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cursor = self.connection.cursor()

    def query(self, argument):
        self.cursor.execute(argument)
        self.connection.commit()
        return self.cursor

    def __del__(self):
        self.connection.close()

"""
def query(query, filename=_filename):
    connection = None

    try:
        connection = sqlite3.connect(_filename)
        cursor = connection.cursor()
        #cursor.execute('SELECT SQLITE_VERSION()')
        cursor.execute(query)
        cols = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
    except sqlite3.Error:
        print('Could not connect do database.')
    finally:
        if connection:
            connection.close()

#todo Store data in SQLite
#todo Class/SQL interface

"""