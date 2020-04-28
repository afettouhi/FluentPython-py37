# Tests for item retrieval using `d[key]` notation::

from StrKeyDict0 import *

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
d['2']

d[4]

d[1]

# Tests for item retrieval using `d.get(key)` notation::

d.get('2')

d.get(4)

d.get(1, 'N/A')

# Tests for the `in` operator::

2 in d

1 in d
