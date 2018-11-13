import unittest
from Crawler import *
from Parser import *


class TestDict(unittest.TestCase):
    def test_shorter_hash(self):
        self.assertEquals(crawler('2'), 'Your hash is shorter than 64')

    def test_longer_hash(self):
        self.assertEquals(crawler('0000000000000000000cdc0d2a9b33c2d4b34b4d4fa8920f074338d0dc1164dd2'),
                          'Your hash is longer than 64')

    def test_invalid_hash1(self):
        self.assertEquals(crawler('0000000000000000000cdc0d2a9b33c2d4b34b4d4fa8920f074338d0dc1164dd'),
                          'invalid hash, 404')

    def test_invalid_hash2(self):
        self.assertEquals(crawler('000000000000000000f061205567dc79c4e718209a568879d66132e016968ac7'),
                          'invalid hash, 404')

    def test_valid_hash1(self):
        self.assertEquals(crawler('000000000000000000f061205567dc79c4e718209a568879d66132e016968ac6'), 'hash valid')

    def test_amount_of_tx(self):
        with open('000000000000000000f061205567dc79c4e718209a568879d66132e016968ac6.bin', 'rb') as blockchain:
            txCount = parse(blockchain)
        self.assertEquals(txCount, 351)


if __name__ == '__main__':
    unittest.main()
