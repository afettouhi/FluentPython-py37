from vector2d_v3_full import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
dumpd

len(dumpd)

v1.typecode = 'f'
dumpf = bytes(v1)
dumpf

len(dumpf)

Vector2d.typecode
