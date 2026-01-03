def primes(limit):
    is_prime = [True] * (limit + 1)

    for i in range(limit + 1):
        if i < 2:
            is_prime[i] = False
        else:
            if is_prime[i]:
                x = 2
                while x * i <= limit:
                    is_prime[x * i] = False
                    x += 1

    return [i for i in range(2, limit + 1) if is_prime[i]]