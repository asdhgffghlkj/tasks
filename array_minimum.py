from typing import Iterable
from typing import Optional


def array_minimum(array: Iterable[int or float]) -> Optional[int]:
    """
    Минимальный элемент последовательности чисел
    :param array: Последовательность чисел
    :return: Значение минимального элемента последовательности
    """
    # your code here
    if (len(array)==0):
        return None
    lead = array[0]
    for i in range(len(array)):
        current = array[i]
        if (current < lead):
            lead = current
    return lead


if __name__ == "__main__":
    assert array_minimum([]) is None
    assert array_minimum([1]) == 1
    assert array_minimum([2]) == 2
    assert array_minimum([-1, 1]) == -1
    assert array_minimum([1, -1]) == -1
    assert array_minimum([1, 1]) == 1
    assert array_minimum([-1, -1]) == -1
    assert array_minimum([1, 2, 1]) == 1
    assert array_minimum([10, 0, 0, 1, 2, 3]) == 0
