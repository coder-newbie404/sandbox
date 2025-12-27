def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    number_to_check = 2
    count = 1
    while count < number:
        number_to_check += 1
        for i in range(2, int(number_to_check**0.5) + 1):
            if number_to_check % i == 0:
                break
        else:
            count += 1
    return number_to_check
        
