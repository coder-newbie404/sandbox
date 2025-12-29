import random
import string


_used_names = set()


def _generate_name():
    while True:
        name = (
            ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            + ''.join(random.choice(string.digits) for _ in range(3))
        )
        if name not in _used_names:
            _used_names.add(name)
            return name


class Robot:
    def __init__(self):
        self.name = _generate_name()

    def reset(self):
        self.name = _generate_name()

