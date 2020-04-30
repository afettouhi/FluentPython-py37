from dis import dis


def f2(a):
    print(a)
    print(b)
    b = 9


dis(f2)
