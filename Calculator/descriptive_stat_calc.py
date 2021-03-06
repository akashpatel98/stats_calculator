from Calculator.calculator import Calculator
from Calculator.functions.descriptive_stat_functions import DescriptiveStatFunctions

class DescriptiveStatCalc(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, input_list: list) -> float:
        self.result.append(DescriptiveStatFunctions.mean(input_list))
        return self.result[-1]

    def median(self, input_list: list) -> float:
        self.result.append(DescriptiveStatFunctions.median(input_list))
        return self.result[-1]

    def mode(self, input_list: list) -> list:
        self.result.append(DescriptiveStatFunctions.mode(input_list))
        return self.result[-1]

    def variance(self, input_list: list) -> float:
        self.result.append(DescriptiveStatFunctions.variance(input_list))
        return self.result[-1]

    def standard_deviation(self, input_list: list) -> float:
        self.result.append(DescriptiveStatFunctions.standard_deviation(input_list))
        return self.result[-1]

    def zScore(self, input_list: list) -> list:
        self.result.append(DescriptiveStatFunctions.zScore(input_list))
        return self.result[-1]


