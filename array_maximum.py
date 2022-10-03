from typing import Iterable
from typing import Optional


def array_maximum(array: Iterable[int]):
    """
    Максимальный элемент последовательности чисел
    :param array: Последовательность чисел
    :return: Значение максимального элемента последовательности
    """
    # your code here
    if (len(array)==0):
        return None
    lead = array[0]
    for i in range(len(array)):
        current = array[i]
        if (current > lead):
            lead = current
    return lead


if __name__ == "__main__":
    assert array_maximum([]) is None
    assert array_maximum([1]) == 1
    assert array_maximum([2]) == 2
    assert array_maximum([-1, 1]) == 1
    assert array_maximum([1, -1]) == 1
    assert array_maximum([1, 1]) == 1
    assert array_maximum([-1, -1]) == -1
    assert array_maximum([1, 2, 1]) == 2
    assert array_maximum([10, 0, 0, 1, 2, 3]) == 10
