import unittest
from hashlib import sha1
import string
import random
from .database import find
from flask import jsonify


def ensure_protocol(url: str):
    s = url
    if url.find("://") == -1:
        s = "http://" + s

    return s


def split_name_from_extension(filename: str):
    dotIndex = filename.rfind('.')
    if dotIndex == -1:
        return filename, ''

    return filename[:dotIndex], filename[dotIndex + 1:]


def generate_url(length: int):
    failedGenerations = 0
    while True:
        url = ''.join(random.choice(string.ascii_letters + string.digits + '+_') for _ in range(length))

        if find("file_url", url) is None:
            return url

        if failedGenerations > 1000:
            length += 1
            failedGenerations = 0

        failedGenerations += 1


def calculate_hash(file):
    return sha1(file)


def failure_to_json():
    return jsonify(success=False, files=[{}])


def record_to_json(fileRecord, url):
    return jsonify(success=True,
                   files=[{"name": fileRecord.realName,
                           "extension": fileRecord.extension,
                           "url": url + fileRecord.url + "." + fileRecord.extension}])


class Test_split_name_from_extension(unittest.TestCase):
    testVals = (
        ('aaaaa', ' bb'),
        ('aa.a.aa', 'bb'),
        ('aaaaa', ''),
    )

    def test(self):
        for filename, extension in self.testVals:
            result = split_name_from_extension('.'.join([filename, extension]))
            self.assertEqual(result[0], filename)
            self.assertEqual(result[1], extension)
