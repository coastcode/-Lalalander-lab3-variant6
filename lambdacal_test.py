import unittest
from hypothesis import given,  strategies
from lambdacal import *


class FactorialTest(unittest.TestCase):
    def test_Factorial(self):
        x=fact(two)
        for _ in range(100):
            x=x.beta()
            print(x)
        print('-----')
        print(two)

    def test_Number(self):
        self.assertEqual(interpret(zero), 0)
        self.assertEqual(interpret(one), 1)
        self.assertEqual(interpret(two), 2)
        self.assertEqual(interpret(three), 3)
        self.assertEqual(interpret(four), 4)
        self.assertEqual(interpret(five), 5)


if __name__ == '__main__':
    unittest.main()
