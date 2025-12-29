def proverb(*insert_words, qualifier=None):
    output = []
    for i in range(len(insert_words) - 1):
        output.append(
            f"For want of a {insert_words[i]} the {insert_words[i + 1]} was lost."
        )
    if insert_words:
        if qualifier:
            output.append(f"And all for the want of a {qualifier} {insert_words[0]}.")
        else:
            output.append(f"And all for the want of a {insert_words[0]}.")
    return output