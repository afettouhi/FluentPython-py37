import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref

wref()

a_set = {2, 3, 4}
wref()

wref() is None

wref() is None
