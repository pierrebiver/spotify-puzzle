import unittest

input1 = [("C1", "D1"), ("D1", "C1")]
input2 = [("C1", "D1"), ("C1", "D1"), ("C1", "D2"), ("D2", "C1")]


class CatVsDog(unittest.TestCase):
    def test_cat_vs_dog(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
