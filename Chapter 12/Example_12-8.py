from frenchdeck2 import FrenchDeck2
import numbers
import io

bool.__mro__


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(bool)

print_mro(FrenchDeck2)

print_mro(numbers.Integral)

print_mro(io.BytesIO)

print_mro(io.TextIOWrapper)
