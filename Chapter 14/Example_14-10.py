from aritprog import ArithmeticProgression
from fractions import Fraction
from decimal import Decimal

ap = ArithmeticProgression(0, 1, 3)
list(ap)

ap = ArithmeticProgression(1, .5, 3)
list(ap)

ap = ArithmeticProgression(0, 1 / 3, 1)
list(ap)

ap = ArithmeticProgression(0, Fraction(1, 3), 1)
list(ap)

ap = ArithmeticProgression(0, Decimal('.1'), .3)
list(ap)
