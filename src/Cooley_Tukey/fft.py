from cmath import cos, sin, pi


def fft(data: list[complex]) -> list[complex]:
    angle: float = (2 * pi) / len(data)
    angle: complex = complex(cos(angle), sin(angle))

    return common_fft(data, angle)


def ifft(data: list[complex]) -> list[complex]:
    degree: int = len(data)

    angle: float = (2 * pi) / degree
    angle: complex = complex(cos(angle), -sin(angle))

    pre_result: list[complex] = common_fft(data, angle)

    result: list[complex] = [(pre_result[index] / degree) for index in range(degree)]

    return result


def common_fft(data: list[complex], angle: complex) -> list[complex]:
    degree: int = len(data)
    half_degree: int = degree // 2

    if degree == 1:
        return data

    data_0 = data[0::2]
    data_1 = data[1::2]

    next_angle: complex = angle * angle

    data_0 = common_fft(data_0, next_angle)
    data_1 = common_fft(data_1, next_angle)

    result: list[complex] = [i for i in range(degree)]

    position: complex = complex(1.0, 0.0)

    for element_index in range(0, half_degree):
        u: complex = data_0[element_index]
        v: complex = position * data_1[element_index]

        result[element_index] = u + v
        result[element_index + half_degree] = u - v

        position *= angle

    return result
