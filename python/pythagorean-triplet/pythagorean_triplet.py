def triplets_with_sum(number):
    for a in range(1, number // 3):
        for b in range(a + 1, number // 2):
            c = number - a - b
            if a * a + b * b == c * c:
                yield [a, b, c]
    return []  # In case no triplets are found
