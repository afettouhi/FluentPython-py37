import itertools

list(itertools.combinations('ABC', 2))

list(itertools.combinations_with_replacement('ABC', 2))

list(itertools.permutations('ABC', 2))

list(itertools.product('ABC', repeat=2))
