import unittest
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    Tests for the FizzBuzz Program
    """

    def test_multiple_of_3_returns_fizz(self):
        result = fizzbuzz.process_num(3)
        self.assertEqual("Fizz", result)


    def test_multiple_of_5_returns_buzz(self):
        result = fizzbuzz.process_num(5)
        self.assertEqual('Buzz', result)


    def test_multiple_of_3_and_5_returns_fizzbuzz(self):
        result = fizzbuzz.process_num(15)
        self.assertEqual('FizzBuzz', result)

    def test_if_other_numbers_return_themselves(self):
        result = fizzbuzz.process_num(2)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
