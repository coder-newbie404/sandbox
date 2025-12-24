def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in sentence.lower():
        if 'a' <= char <= 'z':
            alphabet = alphabet.replace(char, '')
    return len(alphabet) == 0