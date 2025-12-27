def factors(value):
    """Compute the prime factors of a given natural number.

    Args:
        value (int): A natural number greater than 1.

    Returns:
        list: A list of prime factors in ascending order.
    """
    prime_factors = []
    divisor = 2

    while value > 1:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        divisor += 1

    return prime_factors
