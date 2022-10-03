from typing import List
from typing import Optional


def array_premaximum(array: List[int or float]) -> Optional[int]:
    """
    Второй по значению максимальный элемент последовательности чисел
    :param array: Последовательность чисел
    :return: Значение второго по значению максимального элемента последовательности
    """
    # your code here
    if (len(array)<2):
        return None
    if (array[0]>=array[1]):
        vlead=array[1]
    lead = array[0]
    for i in range(1, len(array)):
        current = array[i]
        if (current >= lead):
            vlead = lead
            lead = current
    return vlead


if __name__ == "__main__":
    assert array_premaximum([]) is None
    assert array_premaximum([0]) is None
    assert array_premaximum([-1, 1]) == -1
    assert array_premaximum([1, -1]) == -1
    assert array_premaximum([1, 1]) == 1
    assert array_premaximum([-1, -1]) == -1
    assert array_premaximum([1, 2, 1]) == 1
    assert array_premaximum([0, 1, 2, 3]) == 2
    assert array_premaximum([0, 1, 2, 2]) == 2
    assert array_premaximum([0, 1, 3, 3]) == 3
    assert array_premaximum([4, 5, 3, 2, 1, 0]) == 4
