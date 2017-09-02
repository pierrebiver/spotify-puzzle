import unittest
from zipf_song.zipf_song import zipf_song

inputOne = [(30, "one"), (30, "two"), (15, "three"), (25, "four")]


class MyTestCase(unittest.TestCase):
    def test_zipf_song(self):
        expected = [(25, "four"), (30, "two")]
        self.assertEqual(zipf_song(2, inputOne), expected)


if __name__ == '__main__':
    unittest.main()
