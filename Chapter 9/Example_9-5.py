# inside the Vector2d class


def __format__(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self)
    return '({}, {})'.format(*components)
