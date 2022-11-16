from typing import List


def longest_eps_interval(array: List[int]):
    """
    for num in array[1:]:
        if num = num
    """
    if len(array) == 0:
        return 0
    count = 1
    max_count = 1
    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            cougitnt += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
    return max_count


if __name__ == "__main__":
    assert longest_eps_interval([0, 1, 2, 3, 4, 4, 4, 5, 7, 7, 8, 9]) == 3
    assert longest_eps_interval([0]) == 1
    assert longest_eps_interval([0, 0]) == 2
    assert longest_eps_interval([0, 1, 2]) == 1
    assert longest_eps_interval([-1, 1, 3]) == 1
    assert longest_eps_interval([]) == 0
