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



