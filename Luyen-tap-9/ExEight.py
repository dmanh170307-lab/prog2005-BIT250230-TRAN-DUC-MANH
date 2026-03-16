class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, vector_khac):
        x_moi = self.x + vector_khac.x
        y_moi = self.y + vector_khac.y
        return Vector(x_moi, y_moi)
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3.x, v3.y)