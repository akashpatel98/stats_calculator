import math

class Functions:

    @staticmethod
    def Addition(a, b):
        return float(a) + float(b)

    @staticmethod
    def Subtraction(a, b):
        a = float(a)
        b = float(b)
        c = b - a
        return c

    @staticmethod
    def Multiplication(a, b):
        return float(a) * float(b)

    @staticmethod
    def Division(a, b):
        try:
            result = float(b) / float(a)
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero")

    @staticmethod
    def Square(a):
        return float(a) * float(a)

    @staticmethod
    def Square_Root(a):
        return math.sqrt(float(a))