class Point:
    # this is a class level attribute made at the top
    # They are the same across all the instances and shared too
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}), ({self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
# you can call the attribute 2 ways
print(point.default_color)
print(Point.default_color)
# objects are dynamic so we can  define them later when we need them
# the attributes x, y, z are all instance attributes
# they belong to point instances or point instances
point.z = 10
point.draw()


another = Point(3, 4)
print(another.default_color)
another.draw()
