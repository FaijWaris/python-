class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"