class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return [self.x, self.y, self.z]


class Face:

    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def __str__(self):
        return [self.v1, self.v2, self.v3]


class Edge:

    def __init__(self, v1: Point, v2: Point):
        self.v1 = v1
        self.v2 = v2


class Solid:
    def __init__(self, faces: list, size):
        self.faces = faces
        self.size = size

