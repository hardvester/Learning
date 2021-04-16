# start by test_
import unittest
import calc

class TestCalc(unittest.TestCase):

    # attention, naming convention is required
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
