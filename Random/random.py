import random


class RandomGenerator:
    seed = 10

    def __init__(self):
        pass

    @staticmethod
    def get_random_number():
        return random.random()
