def is_isogram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if string.lower().count(char) > 1:
            return False
    return True