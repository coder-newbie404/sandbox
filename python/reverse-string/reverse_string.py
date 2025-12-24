def reverse(text):
    """Return text reversed."""
    rev = ""
    for char in text:
        rev = char + rev
    return rev
