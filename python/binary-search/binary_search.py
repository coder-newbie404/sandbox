def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
    mid = len(search_list) // 2
    mid_val = search_list[mid]
    if value < mid_val:
        return find(search_list[:mid], value)
    elif value > mid_val:
        return mid + 1 + find(search_list[mid + 1 :], value)
    else:
        return mid