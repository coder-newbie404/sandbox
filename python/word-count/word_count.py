def count_words(sentence):
    separators = {' ', '\n', '\t', '.', ',', '!', '?', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'", "@", "#", "$", "%", "^", "&", "*", "+", "=", "<", ">", "/", "\\"}
    word_count = {}
    word = ''
    contractions = {"can", "won", "it", "they", "we", "you", "i", "isn", "doesn", "don"}

    sentence = sentence.lower()

    for char in sentence:
        if char in separators:
            if word:
                if word in contractions and char == "'":
                    word += char
                else:
                    word_count[word] = word_count.get(word, 0) + 1
                    word = ''
        else:
            word += char

    if word:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count