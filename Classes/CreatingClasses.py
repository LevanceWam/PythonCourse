# When naming classes we follow the Pascal naming method
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
# we can check to see if point is an instance of Point
print(isinstance(point, Point))
