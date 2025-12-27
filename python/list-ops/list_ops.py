def append(list1, list2):
    for item in list2:
        list1 += [item]
    return list1

def concat(lists):
    result = []
    for lst in lists:
        result = append(result, lst)
    return result


def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list += [item]
    return filtered_list

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

def map(function, list):
    mapped_list = []
    for item in list:
        mapped_list += [function(item)]
    return mapped_list


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(result, item)
    return result

def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list = [item] + reversed_list
    return reversed_list