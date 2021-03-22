from Calculator.functions.functions import Functions

class DescriptiveStatFunctions:
    @staticmethod
    def mean(numbers: list) -> float:
        sum = 0.0
        for number in numbers:
            sum = Functions.Addition(sum, number)
        return Functions.Division(sum, len(numbers))
