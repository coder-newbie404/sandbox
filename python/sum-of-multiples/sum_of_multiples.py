def sum_of_multiples(limit, multiples):
    sum = 0
    for num in range(limit):
        for factor in multiples:
            if factor != 0 and num % factor == 0:
                sum += num
                break
    return sum