from random import randint
from unittest import TestCase
from CT_Multiplication import multiply as ct_multiply
from Modulo_Multiplication import multiply as mod_multiply


def generate_data(n: int = 10000):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    polynomial = []

    for i in range(n):
        digit = digits[randint(0, 8)]
        polynomial.append(digit)

    return polynomial


def data_to_int(data: list[int]) -> int:
    return int("".join(map(str, data)))


class RandomMultiplicationTest(TestCase):
    def test_random_numbers(self):
        for i in range(500):
            left: list[int] = generate_data(randint(1, 1000))
            right: list[int] = generate_data(randint(1, 1000))

            ct_result: list[int] = ct_multiply(left, right)
            mod_result: list[int] = mod_multiply(left, right)
            int_result = data_to_int(left) * data_to_int(right)

            self.assertEqual(ct_result, mod_result)
            self.assertEqual(data_to_int(ct_result), int_result)

    def test_equal_degree_numbers(self):
        for i in range(500):
            degree: int = randint(1, 1000)

            left: list[int] = generate_data(degree)
            right: list[int] = generate_data(degree)

            ct_result: list[int] = ct_multiply(left, right)
            mod_result: list[int] = mod_multiply(left, right)
            int_result = data_to_int(left) * data_to_int(right)

            self.assertEqual(ct_result, mod_result)
            self.assertEqual(data_to_int(ct_result), int_result)

    def test_different_degree_numbers(self):
        for i in range(500):
            left_degree: int = randint(1, 950)
            right_degree: int = randint(left_degree + 1, 1000)

            left: list[int] = generate_data(left_degree)
            right: list[int] = generate_data(right_degree)

            ct_result: list[int] = ct_multiply(left, right)
            mod_result: list[int] = mod_multiply(left, right)
            int_result = data_to_int(left) * data_to_int(right)

            self.assertEqual(ct_result, mod_result)
            self.assertEqual(data_to_int(ct_result), int_result)
