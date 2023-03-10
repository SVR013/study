from validate_args import *
import unittest

class TestDecorator(unittest.TestCase):
    def test_va1(self):
        self.assertEqual(add_numbers(4, 5), 9)
        self.assertEqual(add_numbers(18, 10), 28)
        self.assertEqual(add_numbers(10, -7), 3)
        self.assertEqual(add_numbers(10, -18), -8)
    def test_va2(self):
        self.assertEqual(add_numbers(4), 'Мало аргументов')
        self.assertEqual(add_numbers(4, 8, 5), 'Много аргументов')
        self.assertEqual(add_numbers(), 'Мало аргументов')
        self.assertEqual(add_numbers(1, 6, 85, -7), 'Много аргументов')
    def test_va3(self):
        self.assertEqual(add_numbers('4', 5), 'Неправильный тип аргументов')
        self.assertEqual(add_numbers('hello', 'world'), 'Неправильный тип аргументов')
        self.assertEqual(add_numbers(4.25, 8), 'Неправильный тип аргументов')
    @unittest.expectedFailure
    def test_va4(self):
        self.assertEqual(add_numbers('hello world!'), 'Неправильный тип аргументов')
        self.assertEqual(add_numbers(8.96), 'Неправильный тип аргументов')

if __name__ == '__main__':
    unittest.main()