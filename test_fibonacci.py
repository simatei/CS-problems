import unittest
from fibonacci import fib1
from fibonacci2 import fib2
from fibonacci3 import fib3

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib1(1), 1)
        self.assertEqual(fib1(3), 2)

    def test_fibonacci2(self):
        self.assertEqual(fib2(10), 55)
        self.assertEqual(fib2(20), 6765)

    def test_fibonacci3(self):
        self.assertEqual(fib3(1), 1)
        self.assertEqual(fib3(3), 2)


if __name__ == '__main__':
    unittest.main()