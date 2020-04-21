class Point:
    # instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

# this is call a decorator
# this is used to make it a class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

# instance method
    def draw(self):
        print(f"Point ({self.x}), ({self.y})")


# using a class reference
point = Point.zero()
# we call an instance method by using a object, an instance of the point method
point.draw()
