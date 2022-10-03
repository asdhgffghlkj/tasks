from typing import Iterable
from typing import Optional


def array_preminimum(array: Iterable[int or float]) -> Optional[int or float]:
    """
    Второй по значению минимальный элемент последовательности чисел
    :param array: Последовательность чисел
    :return: Значение второго по значению минимального элемента последовательности
    """
    # your code here
    if (len(array)<2):
        return None
    if (array[0]<=array[1]):
        vlead=array[1]
    lead = array[0]
    for i in range(1, len(array)):
        current = array[i]
        if (current <= lead):
            vlead = lead
            lead = current
    return vlead


if __name__ == "__main__":
    assert array_preminimum([]) is None
    assert array_preminimum([0]) is None
    assert array_preminimum([-1, 1]) == 1
    assert array_preminimum([1, -1]) == 1
    assert array_preminimum([1, 1]) == 1
    assert array_preminimum([-1, -1]) == -1
    assert array_preminimum([1, 2, 1]) == 1
    assert array_preminimum([0, -1, -2, -3]) == -2
    assert array_preminimum([0, -1, -2, -2]) == -2
    assert array_preminimum([0, -1, -3, -3]) == -3
