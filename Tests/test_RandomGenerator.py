import unittest

from helpers.RandomGenerator import RandomGenerator


class RandomGeneratorTestCase(unittest.TestCase):

    def test_random_generator(self):
        randomNumber = RandomGenerator.get_random_number(5)
        self.assertEqual(randomNumber, 5)

    def test_random_generator_static_variable(self):
        static_variable = RandomGenerator.this_value

        self.assertEqual(static_variable, 5)
