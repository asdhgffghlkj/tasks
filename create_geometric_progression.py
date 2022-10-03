from typing import List


def create_geometric_progression(
        first_element: int or float,
        difference: int or float,
        progression_length: int
) -> List[int]:
    """
    Функция создаёт список, элементы которого составляют часть геометрической прогрессии
    :param first_element: Первый элемент искомой прогрессии
    :param difference: Знаменатель искомой прогрессии
    :param progression_length: Длина желаемой часть геометрической прогрессии
    :return: Список, элементы которого составляют часть геометрической прогрессии
    """
    # your code here
    thelist = list()
    thelist.append(first_element)
    for i in range(1, progression_length):
        newelement = difference * thelist[i - 1]
        thelist.append(newelement)
    return thelist


if __name__ == "__main__":
    assert create_geometric_progression(0, 1, 2) == [0, 0]
    assert create_geometric_progression(0, 1, 8) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert create_geometric_progression(1, 2, 5) == [1, 2, 4, 8, 16]
    assert create_geometric_progression(-1, 2, 5) == [-1, -2, -4, -8, -16]
    assert create_geometric_progression(1, -2, 5) == [1, -2, 4, -8, 16]
