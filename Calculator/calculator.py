from Calculator.functions.functions import Functions
#from Operations.Addition import addition
#from Operations.Subtraction import subtraction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Functions.Addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Functions.Subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Functions.Multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = round(Functions.Division(a, b), 9)
        return self.result

    def square(self, a):
        self.result = Functions.Square(a)
        return self.result

    def squareRoot(self, a):
        self.result = Functions.Square_Root(a)
        return self.result