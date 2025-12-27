def decode(string):
    if not string:
        return ""

    decoded = []
    count = ''
    
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count:
                decoded.append(char * int(count))
                count = ''
            else:
                decoded.append(char)

    return ''.join(decoded)


def encode(string):
    if not string:
        return ""

    encoded = []
    count = 1
    previous_char = string[0]

    for char in string[1:]:
        if char == previous_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{previous_char}")
            else:
                encoded.append(previous_char)
            previous_char = char
            count = 1

    # Handle the last sequence
    if count > 1:
        encoded.append(f"{count}{previous_char}")
    else:
        encoded.append(previous_char)

    return ''.join(encoded)
