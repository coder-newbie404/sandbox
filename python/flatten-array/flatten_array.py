def flatten(iterable):
    if not isinstance(iterable, list):
        return [iterable]
    else:
        result = []
        for item in iterable:
            if item is None:
                continue
            else:
                result.extend(flatten(item))
        return result
    