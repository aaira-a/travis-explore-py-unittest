
import unittest

from project.calculator import (
    add,
)


class CalculatorTests(unittest.TestCase):

    def test_add_two_integers(self):
        self.assertEqual(5, add(2, 3))
