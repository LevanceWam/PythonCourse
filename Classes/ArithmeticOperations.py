class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
# this will not print the Results it because we don't have the __str__ method
print(point + other)
combined = point + other
print(combined)
