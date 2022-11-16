from typing import List


def longest_eps_1_interval(array: List[int]):
    if len(array) == 0:
        return 0
    count = 1
    max_count = 1
    core = 0
    for i in range(1, len(array)):
        print(str(i+1) + " / " + str(count))
        if array[i] - array[core] < 2:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
            core = i
    print(max_count)
    return max_count


if __name__ == "__main__":
    assert longest_eps_1_interval([0, 1, 2, 3, 4, 4, 4, 5, 7, 7, 8, 9]) == 4
    assert longest_eps_1_interval([0]) == 1
    assert longest_eps_1_interval([0, 0]) == 2
    assert longest_eps_1_interval([0, 1, 2]) == 2
    assert longest_eps_1_interval([-1, 1, 3]) == 1
    assert longest_eps_1_interval([]) == 0
    assert longest_eps_1_interval([-1, 1]) == 1
    assert longest_eps_1_interval([-1, 0, 1]) == 2
