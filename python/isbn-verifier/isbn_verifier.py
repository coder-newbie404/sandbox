def is_valid(isbn):
    cleaned = isbn.replace("-", "")
    for char in cleaned[:-1]:
        if not char.isdigit():
            return False
    if len(cleaned) != 10:
        return False
    total = 0
    for i, char in enumerate(cleaned):
        if char == 'X' and i == 9:
            total += 10
        elif char.isdigit():
            total += int(char) * (10 - i)
        else:
            return False
    return total % 11 == 0