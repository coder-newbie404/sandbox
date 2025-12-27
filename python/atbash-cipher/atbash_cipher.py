def encode(plain_text):
    plain_alphabet = dict(zip(
        'abcdefghijklmnopqrstuvwxyz',
        'zyxwvutsrqponmlkjihgfedcba'
    ))

    cleaned = []
    count = 0
    for char in plain_text.lower():
        if char.isalpha():
            cleaned.append(plain_alphabet[char])
        elif char.isdigit():
            cleaned.append(char)
        else:
            continue
        if count == 4:
            cleaned.append(' ')
            count = 0
        else:
            count += 1
    return ''.join(cleaned).rstrip()


def decode(ciphered_text):
    cipher_alphabet = dict(zip(
        'zyxwvutsrqponmlkjihgfedcba',
        'abcdefghijklmnopqrstuvwxyz'
    ))
    decoded = []
    for char in ciphered_text.lower():
        if char.isalpha():
            decoded.append(cipher_alphabet[char])
        elif char == ' ':
            continue
        else:
            decoded.append(char)
    return ''.join(decoded)
