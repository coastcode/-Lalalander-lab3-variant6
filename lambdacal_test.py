import unittest
from lambdacal import *


class FactorialTest(unittest.TestCase):
    def test_Church_number(self):
        self.assertEqual(interpret(Church_0()), 0)
        self.assertEqual(interpret(Church_1), 1)
        self.assertEqual(interpret(Church_2), 2)
        self.assertEqual(interpret(Church_3), 3)
        self.assertEqual(interpret(Church_4), 4)
        self.assertEqual(interpret(Church_5), 5)

    def test_Increment(self):
        self.assertEqual(interpret(SUCC(Church_3)), 4)
        self.assertEqual(interpret(SUCC(Church_0)), 1)
        self.assertEqual(interpret(SUCC(Church_5)), 6)

    def test_Addition(self):
        self.assertEqual(interpret(PLUS(Church_0)(Church_1)), 1)
        self.assertEqual(interpret(PLUS(Church_2)(Church_3)), 5)
        self.assertEqual(interpret(PLUS(Church_5)(Church_1)), 6)

    def test_Multiplication(self):
        self.assertEqual(interpret(MULT(Church_0)(Church_3)), 0)
        self.assertEqual(interpret(MULT(Church_2)(Church_3)), 6)
        self.assertEqual(interpret(MULT(Church_5)(Church_5)), 25)

    def test_Decrement(self):
        self.assertEqual(interpret(PRED(Church_5)), 4)
        self.assertEqual(interpret(PRED(Church_1)), 0)

    def test_Logic_And(self):
        self.assertEqual(predicate(AND(Church_False)(Church_True)), False)
        self.assertEqual(predicate(AND(Church_True)(Church_True)), True)

    def test_Logic_Or(self):
        self.assertEqual(predicate(OR(Church_True)(Church_False)), True)
        self.assertEqual(predicate(OR(Church_True)(Church_True)), True)
        self.assertEqual(predicate(OR(Church_False)(Church_False)), False)

    def test_Logic_Not(self):
        self.assertEqual(predicate(NOT(Church_True)), False)
        self.assertEqual(predicate(NOT(Church_False)), True)

    def test_Iszero(self):
        self.assertEqual(predicate(ISZERO(Church_0)), True)
        self.assertEqual(predicate(ISZERO(Church_5)), False)

    def test_Factorial(self):
        self.assertEqual(interpret(FACT(Church_5)), 120)
        self.assertEqual(interpret(FACT(PLUS(Church_5)(Church_1))), 720)


if __name__ == '__main__':
    unittest.main()
