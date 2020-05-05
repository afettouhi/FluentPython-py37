"""Example 16-6
A coroutine to compute a running average

    >>> coro_avg = averager()  1
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)  2
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)  3
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

"""

from coroutil import coroutine


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
