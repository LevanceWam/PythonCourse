class Animal:
    def __init__(self):
        print("Animal Constructor")
        # Mammal would not be able to use the constructor from here without line 16
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # Here we are allowing the mammal class to call a upon the constructor from animal
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
