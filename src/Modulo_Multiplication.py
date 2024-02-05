from Modulo.fft import fft, ifft


def multiply(left: list[int], right: list[int]) -> list[int]:
    polynomial = calculate_multiplication(left, right)

    carry = 0

    for i in range(0, len(polynomial)):
        index = len(polynomial) - (i + 1)
        number = polynomial[index] + carry
        carry = number // 10
        polynomial[index] = number % 10

    if carry > 0:
        polynomial = [carry] + polynomial

    while carry >= 10:
        polynomial = [carry % 10] + polynomial
        carry //= 10

    return polynomial


def get_correct_length(current_length: int) -> int:
    n = 1

    while n < current_length:
        n *= 2

    return n * 2


def correct_length(data: list[int], new_length: int) -> list[int]:
    result: list[int] = [0 for i in range(new_length)]

    for i in range(0, len(data)):
        result[i] = data[i]

    return result


def strip_non_significant_nulls(a: list[int]):
    index = len(a) - 1

    while index >= 0:
        if a[index] == 0:
            a.pop(index)
            index -= 1
            continue

        break

    return a


def calculate_multiplication(left: list[int], right: list[int]) -> list[int]:
    max_length: int = max(len(left), len(right))

    n = get_correct_length(max_length)

    left_complex = correct_length(left, n)
    right_complex = correct_length(right, n)

    left_fft = fft(left_complex)
    right_fft = fft(right_complex)

    coefficients: list[complex] = [complex(0.0, 0.0) for i in range(n)]

    for i in range(n):
        coefficients[i] = left_fft[i] * right_fft[i]

    result: list[int] = ifft(coefficients)

    return strip_non_significant_nulls(result)
