class File:
    def __init__(self, hash, realName, extension, url):
        self.hash = hash
        self.realName = realName
        self.extension = extension
        self.url = url

    @staticmethod
    def from_DB(record):
        return File(record[0], record[1], record[2], record[3])
