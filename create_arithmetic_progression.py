from typing import List


def create_arithmetic_progression(
        first_element: int or float,
        difference: int or float,
        progression_length: int
) -> List[int]:
    """
    Функция создаёт список, элементы которого составляют часть арифметической прогрессии
    :param first_element: Первый элемент искомой прогрессии
    :param difference: Разность искомой прогрессии
    :param progression_length: Длина желаемой часть арифметической прогрессии
    :return: Список, элементы которого составляют часть арифметической прогрессии
    """
    thelist = list()
    thelist.append(first_element)
    for i in range(1, progression_length):
        newelement = difference + thelist[i-1]
        thelist.append(newelement)
    return thelist


if __name__ == "__main__":
    assert create_arithmetic_progression(0, 1, 1) == [0]
    assert create_arithmetic_progression(0, 1, 2) == [0, 1]
    assert create_arithmetic_progression(0, 1, 8) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert create_arithmetic_progression(-3, 2, 4) == [-3, -1, 1, 3]
    assert create_arithmetic_progression(-1, 2, 5) == [-1, 1, 3, 5, 7]
