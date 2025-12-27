def square_root(number):
    for i in range(number // 2 + 1):
        if i * i == number:
            return i
    return number