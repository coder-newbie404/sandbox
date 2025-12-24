def score(x, y):
    """Compute the score between two values.

    Args:
        x: First value.
        y: Second value.

    Returns:
        A float representing the score.
    """
    distance = (x ** 2 + y ** 2) ** 0.5
    if distance <= 1:
        return 10.0
    elif distance <= 5:
        return 5.0
    elif distance <= 10:
        return 1.0
    else:
        return 0.0