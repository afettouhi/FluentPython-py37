def chain(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
list(chain(s, t))
