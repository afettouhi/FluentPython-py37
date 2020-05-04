import itertools
import operator

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

list(itertools.accumulate(sample))

list(itertools.accumulate(sample, min))

list(itertools.accumulate(sample, max))

list(itertools.accumulate(sample, operator.mul))

list(itertools.accumulate(range(1, 11), operator.mul))
