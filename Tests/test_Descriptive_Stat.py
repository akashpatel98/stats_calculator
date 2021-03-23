import unittest
import random
import statistics
from Calculator.descriptive_stat_calc import DescriptiveStatCalc
from scipy.stats import zscore as scipy_zscore


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

    def testMode(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = statistics.mode(rList)
        actualVal = self.calculator.mode(rList)
        self.assertEqual(expectedVal, actualVal)

    def testVariance(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = statistics.pvariance(rList)
        actualVal = self.calculator.variance(rList)
        self.assertAlmostEqual(expectedVal, actualVal)

    def test_Standard_Deviation(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = statistics.pstdev(rList)
        actualVal = self.calculator.standard_deviation(rList)
        self.assertAlmostEqual(expectedVal, actualVal)

    def test_zScore(self):
        rList = []
        for i in range(0, 100000):
            rNumber = random.randint(0, 1000)
            rList.append(rNumber)
        expectedVal = scipy_zscore(rList)
        actualVal = self.calculator.zScore(rList)
        self.assertEqual(expectedVal.size, len(actualVal))
        for i in range(0, expectedVal.size):
            self.assertAlmostEqual(expectedVal[i], actualVal[i])







