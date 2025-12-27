def rows(letter):
    size = ord(letter) - ord('A')
    diamond_rows = []

    for i in range(size + 1):
        current_letter = chr(ord('A') + i)
        if i == 0:
            row = ' ' * size + current_letter + ' ' * size
        else:
            spaces_between = ' ' * (2 * i - 1)
            row = ' ' * (size - i) + current_letter + spaces_between + current_letter + ' ' * (size - i)
        diamond_rows.append(row)

    for i in range(size - 1, -1, -1):
        diamond_rows.append(diamond_rows[i])

    return diamond_rows
