import unittest
from number_output.number_output import get_number_output

class TestNumberOutput(unittest.TestCase):
    def test_threefive_output(self):
        self.assertEqual(get_number_output(15), "ThreeFive")
        self.assertEqual(get_number_output(30), "ThreeFive")
        self.assertEqual(get_number_output(45), "ThreeFive")
        self.assertEqual(get_number_output(60), "ThreeFive")
        self.assertEqual(get_number_output(75), "ThreeFive")
        self.assertEqual(get_number_output(90), "ThreeFive")

    def test_three_output(self):
        self.assertEqual(get_number_output(3), "Three")
        self.assertEqual(get_number_output(6), "Three")
        self.assertEqual(get_number_output(18), "Three")
        self.assertEqual(get_number_output(36), "Three")
        self.assertEqual(get_number_output(63), "Three")
        self.assertEqual(get_number_output(99), "Three")

    def test_five_output(self):
        self.assertEqual(get_number_output(5), "Five")
        self.assertEqual(get_number_output(10), "Five")
        self.assertEqual(get_number_output(25), "Five")
        self.assertEqual(get_number_output(50), "Five")
        self.assertEqual(get_number_output(95), "Five")
        self.assertEqual(get_number_output(100), "Five")

    def test_number_output(self):
        for i in [1, 2, 97, 23, 46, 73]:
            self.assertEqual(get_number_output(i), i)

if __name__ == "__main__":
    unittest.main()