from vector_v11 import Vector

v1 = Vector([1, 2, 3])
v1_alias = v1
id(v1)

v1 += Vector([4, 5, 6])
v1

id(v1)

v1_alias

v1 *= 11
v1

id(v1)
