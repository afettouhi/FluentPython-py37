class C:
    pass


obj = C()


def func(): pass


sorted(set(dir(func)) - set(dir(obj)))
