def add(moment):
    from datetime import timedelta

    gigasecond = 10**9
    return moment + timedelta(seconds=gigasecond)
