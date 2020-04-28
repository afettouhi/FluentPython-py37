from factorial import *

fact = factorial

list(map(fact, range(6)))

[fact(n) for n in range(6)]

list(map(factorial, filter(lambda n: n % 2, range(6))))

[factorial(n) for n in range(6) if n % 2]
