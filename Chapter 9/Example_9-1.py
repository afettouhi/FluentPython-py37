from vector2d_v0 import Vector2d

v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1

x, y

v1

v1_clone = eval(repr(v1))

v1 == v1_clone

print(v1)

octets = bytes(v1)

octets

abs(v1)

bool(v1), bool(Vector2d(0, 0))
