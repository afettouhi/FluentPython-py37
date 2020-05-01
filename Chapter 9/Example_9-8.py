# inside class Vector2d:


def __hash__(self):
    return hash(self.x) ^ hash(self.y)
