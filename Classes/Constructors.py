# Constructors are a special method that is called when we make a new point object
class Point:
    # self is a reference to the current point object
    # this is a magic method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}), ({self.y})")


point = Point(1, 2)
print(point.x)
point.draw()
