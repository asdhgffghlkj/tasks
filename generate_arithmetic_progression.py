def generate_arithmetic_progression(first_elem, difference, n):
    result = []
    if n == 0:
        return result
    for i in range(n):
        result.append(first_elem + difference * i)
    return result


print(generate_arithmetic_progression(10, 10, 4))
