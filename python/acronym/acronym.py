def abbreviate(words):
    acronym = '' + words[0]
    for i in range(1, len(words)):
        if words[i - 1] in [" ", "-", "_", ","] and words[i].isalpha():
            acronym += words[i].upper()
    return acronym
