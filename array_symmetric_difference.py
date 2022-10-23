from typing import List


def array_symmetric_difference(first_array: List[int], second_array: List[int]) -> List[int]:
    """
    Возвращает список, который содержит все элементы симметрической разницы списков first_array и second_array.
    Т. е. все элементы, которые находятся только в одном из списков first_array, либо second_array. Списки first_array и
    second_array не содержат повторяющихся элементов
    :param first_array: Первый список
    :param second_array: Второй список
    :return: Список с элементами симметрической разности
    """
    pass


if __name__ == "__main__":
    assert array_symmetric_difference([], []) == []
    assert array_symmetric_difference([], [1]) == [1]
    assert array_symmetric_difference([1], []) == [1]
    assert array_symmetric_difference([1], [1]) == []
    assert array_symmetric_difference([0, 1], [1]) == [0]
    assert array_symmetric_difference([1], [1, 2]) == [2]
    assert set(array_symmetric_difference([0, 1], [1, 2])) == {0, 2}
    assert set(array_symmetric_difference([0, 2], [1, 3])) == {0, 1, 2, 3}
    assert set(array_symmetric_difference([0, 3], [1, 2])) == {0, 1, 2, 3}
    assert set(array_symmetric_difference([0, 1, 2, 3], [])) == {0, 1, 2, 3}
    assert set(array_symmetric_difference([], [0, 1, 2, 3])) == {0, 1, 2, 3}
    assert set(array_symmetric_difference([0, 1, 2, 3], [1, 2, 3, 4])) == {0, 4}
    assert set(array_symmetric_difference([0, 1, 2, 3], [1, 2, 3, 4])) == {0, 4}
