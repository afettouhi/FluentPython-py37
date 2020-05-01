from itertools import zip_longest

zip(range(3), 'ABC')

list(zip(range(3), 'ABC'))

list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))

list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
