def rotate(text, key):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated_char = chr((ord(char) - base + key) % 26 + base)
            result.append(rotated_char)
        else:
            result.append(char)

    return ''.join(result)