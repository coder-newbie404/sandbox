def commands(binary_str):
    action = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump'
    }
    result = []
    binary_str = binary_str[::-1]
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            if i == 4:
                result.reverse()
            else:
                result.append(action[i])

    return result
        
