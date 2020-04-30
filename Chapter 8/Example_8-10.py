from copy import deepcopy

a = [10, 20]
b = [a, 30]
a.append(b)
a

c = deepcopy(a)
c
