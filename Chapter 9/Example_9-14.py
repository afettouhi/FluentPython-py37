from vector2d_v3_full import Vector2d


class ShortVector2d(Vector2d):
    typecode = 'f'


sv = ShortVector2d(1 / 11, 1 / 27)
sv
ShortVector2d(0.09090909090909091, 0.037037037037037035)
len(bytes(sv))
