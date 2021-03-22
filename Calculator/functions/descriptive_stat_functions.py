from Calculator.functions.functions import Functions

class DescriptiveStatFunctions:
    @staticmethod
    def mean(numbers: list) -> float:
        sum = 0.0
        for number in numbers:
            sum = Functions.Addition(sum, number)
        return Functions.Division(sum, len(numbers))

    @staticmethod
    def median(numbers: list) -> float:
        numbers = sorted(numbers)
        if len(numbers) % 2 == 1:
            midIndex = int(Functions.Division(len(numbers) - 1, 2))
            median = numbers[midIndex]
        else:
            leftMidIndex = int(Functions.Subtraction(Functions.Division(len(numbers) - 1, 2), 0.5))
            rightMidIndex = int(Functions.Addition(Functions.Division(len(numbers) - 1, 2), 0.5))
            median = Functions.Division(Functions.Addition(numbers[leftMidIndex], numbers[rightMidIndex]), 2)
        return float(median)

    @staticmethod
    def mode(numbers: list) -> list:
        d = {}
        for number in numbers:
            if number in d.keys():
                d[number] += 1
            else:
                d[number] = 1
        occurrences = 0
        for number in numbers:
            if d[number] > occurrences:
                occurrences = d[number]
        mode = []
        for number in d.keys():
            if d[number] == occurrences:
                mode.append(number)
        return mode

    @staticmethod
    def variance(numbers: list) -> float:
        mean = DescriptiveStatFunctions.mean(numbers)
        SquareDiff = []
        for number in numbers:
            SquareDiff.append(Functions.Square(Functions.Subtraction(mean, number)))
        varience = Functions.Division(sum(SquareDiff), len(numbers))
        return varience

