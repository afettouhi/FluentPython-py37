import functools
import operator

n = 0
for i in range(1, 6):
    n ^= i

n

functools.reduce(lambda a, b: a^b, range(6))
