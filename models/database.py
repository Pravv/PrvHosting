from .file_record import File
import sqlite3


class Database:
    def __init__(self):
        self.conn = {}
        self.queries = {}

    def cursor(self):
        return self.conn.cursor()

    def init(self):
        self.conn = sqlite3.connect('db_files/prv.db', check_same_thread=False)
        self.queries = {
            "Find_file_hash": "SELECT * FROM files WHERE hash = ? LIMIT 1;",
            "Find_file_url": "SELECT * FROM files WHERE url = ? LIMIT 1;",

            "Find_url_hash": "SELECT * FROM shortened WHERE hash = ? LIMIT 1;",
            "Find_url_short": "SELECT * FROM shortened WHERE short = ? LIMIT 1;",

            "Insert_file": "INSERT INTO files VALUES (?, ?, ?, ?);",
            "Insert_short": "INSERT INTO shortened VALUES (?, ?, ?);",
        }


database = Database()
database.init()


def find(where, what):
    cursor = database.cursor()

    cursor.execute(database.queries['Find_' + where], (what,))
    database.conn.commit()

    result = cursor.fetchone()
    cursor.close()

    return result


def add_short(short, original, hash):
    cursor = database.cursor()

    cursor.execute(database.queries['Insert_short'], (short, original, hash))
    database.conn.commit()

    result = cursor.lastrowid
    cursor.close()

    return result


def add_file(fileRecord: File):
    cursor = database.cursor()

    cursor.execute(database.queries['Insert_file'], (fileRecord.hash,
                                                     fileRecord.realName,
                                                     fileRecord.extension,
                                                     fileRecord.url))
    database.conn.commit()

    result = cursor.lastrowid
    cursor.close()

    return result
