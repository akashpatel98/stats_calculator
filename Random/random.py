import random


class RandomGenerator:
    seed = 10

    def __init__(self):
        pass

    @staticmethod
    def get_random_number(seed):
        random.seed(seed)
        return random.random()
