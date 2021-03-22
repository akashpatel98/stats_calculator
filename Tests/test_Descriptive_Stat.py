import unittest
import random
import statistics
from Calculator.descriptive_stat_calc import DescriptiveStatCalc


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = DescriptiveStatCalc()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, DescriptiveStatCalc)

    def testMean(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = statistics.mean(rList)
        actualVal = self.calculator.mean(rList)
        self.assertEqual(expectedVal, actualVal)

    def testMedian(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = statistics.median(rList)
        actualVal = self.calculator.median(rList)
        self.assertEqual(expectedVal, actualVal)





