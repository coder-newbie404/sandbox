def transpose(text):
    if len(text) == 0:
        return text
    substrings = []
    while len(text) > 0:
        newline_index = text.find('\n')
        if newline_index == -1:
            substrings.append(text)
            break
        else:
            substrings.append(text[:newline_index])
        text = text[newline_index + 1:]

    longeest_substring_length = len(substrings[-1])
    for i, substring in reversed(list(enumerate(substrings[:-1]))):
        if len(substring) < longeest_substring_length:
            while len(substring) < longeest_substring_length:
                substring += ' '
            substrings[i] = substring
        if len(substring) > longeest_substring_length:
            longeest_substring_length = len(substring)

    output = ''
    for i in range(longeest_substring_length):
        for substring in substrings:
            if i < len(substring):
                output += substring[i]
        output += '\n'
    return output[:-1].rstrip()