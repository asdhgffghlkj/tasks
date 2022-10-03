from typing import List


def check_if_array_is_an_arithmetic_progression(array: List[int or float]) -> bool:
    """
    Определить, является ли последовательность частью арифметической прогрессии
    :param array: Последовательность чисел
    :return: True, если является, False иначе
    """
    # your code here
    if (len(array)<3):
        return True
    diff = array[1]-array[0]
    for i in range(1, len(array)):
        if (array[i]-array[i-1]!=diff):
            return False
    return True

if __name__ == "__main__":
    assert check_if_array_is_an_arithmetic_progression([])
    assert check_if_array_is_an_arithmetic_progression([0])
    assert check_if_array_is_an_arithmetic_progression([-1, 1])
    assert check_if_array_is_an_arithmetic_progression([1, -1])
    assert check_if_array_is_an_arithmetic_progression([1, 1])
    assert check_if_array_is_an_arithmetic_progression([-1, -1])
    assert not check_if_array_is_an_arithmetic_progression([1, 2, 1])
    assert check_if_array_is_an_arithmetic_progression([0, -1, -2, -3])
    assert not check_if_array_is_an_arithmetic_progression([0, -1, -2, -2])
    assert not check_if_array_is_an_arithmetic_progression([0, -1, -3, -3])
