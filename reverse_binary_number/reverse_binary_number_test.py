import unittest
from reverse_binary_number.reverse_binary_number import reverse_binary_number, binary_to_number, number_to_binary


class ReverseBinaryNumber(unittest.TestCase):
    def test_number_to_binary(self):
        self.assertEqual(number_to_binary(1), 1)
        self.assertEqual(number_to_binary(2), 10)
        self.assertEqual(number_to_binary(3), 11)
        self.assertEqual(number_to_binary(324), 101000100)

    def test_binary_to_number(self):
        self.assertEqual(binary_to_number(10), 2)
        self.assertEqual(binary_to_number(11), 3)
        self.assertEqual(binary_to_number(101000100), 324)

    def test_reverse_binary_to_number(self):
        self.assertEqual(reverse_binary_number(13), 11)


if __name__ == '__main__':
    unittest.main()
