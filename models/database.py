from .file_record import File
import sqlite3
import unittest


def find(filename):
    return filename + filename


def add_to_database(file: File, url):
    return True


def init():
    return {
        "Findhash": "SELECT * FROM files WHERE hash = ? LIMIT 1;",
        "Findurl": "SELECT * FROM files WHERE url = ? LIMIT 1;",
        "InsertFile": "INSERT INTO files VALUES (?, ?, ?, ?);",
        "FindIn": "SELECT * FROM files WHERE hash IN (?);"
    }


class Test_init(unittest.TestCase):

    def test(self):
        print(init()['Findhash'])
