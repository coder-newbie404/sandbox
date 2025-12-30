def egg_count(display_value):
    string = ""
    while display_value > 0:
        string += str(display_value % 2)
        display_value //= 2
    return string.count('1')