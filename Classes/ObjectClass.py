class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, base
# Mammal: child, sub


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
# We can use this to see if an object is a instance of a given class
print(isinstance(m, Animal))
# We can use this to see if an object is a subclass of a class
print(issubclass(Mammal, Animal))
