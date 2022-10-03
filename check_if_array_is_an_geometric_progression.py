from typing import Iterable


def check_if_array_is_an_geometric_progression(array: Iterable[int or float]) -> bool:
    """
    Определить, является ли последовательность частью геометрической прогрессии
    :param array: Последовательность чисел
    :return: True, если является, False иначе
    """
    # your code here
    for i in range(len(array)):
        if array[i] == 0:
            return 0
    if (len(array)<3):
        return True
    rat = array[1]/array[0]
    for i in range(1, len(array)):
        if (array[i]/array[i-1]!=rat):
            return 0
    return 1


if __name__ == "__main__":
    assert check_if_array_is_an_geometric_progression([1])
    assert check_if_array_is_an_geometric_progression([-1])
    assert check_if_array_is_an_geometric_progression([2])
    assert check_if_array_is_an_geometric_progression([-3])
    assert check_if_array_is_an_geometric_progression([-1, 1])
    assert check_if_array_is_an_geometric_progression([1, -1])
    assert not check_if_array_is_an_geometric_progression([0, 1])
    # assert check_if_array_is_an_geometric_progression([1, 0])
    # assert check_if_array_is_an_geometric_progression([1, 0, 0])
    # assert check_if_array_is_an_geometric_progression([1, 0, 0, 0])
    assert check_if_array_is_an_geometric_progression([1, 1])
    assert check_if_array_is_an_geometric_progression([1, 1, 1])
    assert check_if_array_is_an_geometric_progression([-1, -1])
    assert not check_if_array_is_an_geometric_progression([-1, -1, 0])
    assert not check_if_array_is_an_geometric_progression([-1, -2, -3])
    assert not check_if_array_is_an_geometric_progression([1, 2, 1])
    assert not check_if_array_is_an_geometric_progression([0, -1, -2, -3])
    assert not check_if_array_is_an_geometric_progression([0, -1, -2, -2])
    assert not check_if_array_is_an_geometric_progression([0, -1, -3, -3])
    assert check_if_array_is_an_geometric_progression([1, 2, 4])
    assert check_if_array_is_an_geometric_progression([1, 2, 4, 8])
    assert check_if_array_is_an_geometric_progression([1, -2, 4, -8])
    assert not check_if_array_is_an_geometric_progression([1, -2, 4, -8.01])
    assert not check_if_array_is_an_geometric_progression([1, 2, 4, -8])
    assert not check_if_array_is_an_geometric_progression([1, 2, 4, 0])
    assert not check_if_array_is_an_geometric_progression([float("Inf"), 1, float("Inf")])
    pi_progression = []
    elem = 1
    for _ in range(200):
        pi_progression.append(elem)
        elem = elem * 2
    assert check_if_array_is_an_geometric_progression(pi_progression)
