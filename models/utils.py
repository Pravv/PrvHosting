import unittest
from hashlib import sha1
import string
import random
from .database import find


def split_name_from_extension(filename: str):
    dotIndex = filename.rfind('.')
    if dotIndex == -1:
        return filename, ''

    return filename[:dotIndex], filename[dotIndex + 1:]


def generate_url(length: int):
    failedGenerations = 0
    while True:
        url = ''.join(random.choice(string.ascii_letters + string.digits + '+_') for _ in range(length))
        if not find("url"):
            return url

        if failedGenerations > 1000:
            length += 1
            failedGenerations = 0

        failedGenerations += 1


def calculate_hash(file):
    return sha1(file)


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
