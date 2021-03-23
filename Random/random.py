import random


class RandomGenerator:

    def __init__(self):
        pass

    @staticmethod
    def get_random_number(s: int) -> float:
        random.seed(s)
        return random.random()

    @staticmethod
    def get_random_number(s: int) -> float:
        random.seed(s)
        return random.random()