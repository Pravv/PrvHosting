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

            "Get_user_files": "SELECT * FROM files WHERE user = ?",
            "Get_user_short": "SELECT * FROM shortened WHERE user = ?;",

            "Insert_file": "INSERT INTO files VALUES (?, ?, ?, ?, ?);",
            "Insert_short": "INSERT INTO shortened VALUES (?, ?, ?, ?);",
        }


database = Database()
database.init()


def get_user_files(userID):
    cursor = database.cursor()

    cursor.execute(database.queries["Get_user_files"], (userID,))
    database.conn.commit()
    files = cursor.fetchall()

    cursor.execute(database.queries["Get_user_short"], (userID,))
    database.conn.commit()
    shorts = cursor.fetchall()

    cursor.close()

    return files, shorts


def find(where, what):
    cursor = database.cursor()

    cursor.execute(database.queries['Find_' + where], (what,))
    database.conn.commit()

    result = cursor.fetchone()
    cursor.close()

    return result


def add_short(short, original, hash, userID):
    cursor = database.cursor()

    cursor.execute(database.queries['Insert_short'], (short, original, hash, userID))
    database.conn.commit()

    result = cursor.lastrowid
    cursor.close()

    return result


def add_file(fileRecord: File, userID):
    cursor = database.cursor()

    cursor.execute(database.queries['Insert_file'], (fileRecord.hash,
                                                     fileRecord.realName,
                                                     fileRecord.extension,
                                                     fileRecord.url,
                                                     userID))
    database.conn.commit()

    result = cursor.lastrowid
    cursor.close()

    return result
