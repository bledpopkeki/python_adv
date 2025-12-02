class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("abs")

    def description(self):
        print(f"asdas{self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("wof wof")

    def description(self):
        super().description()

        print(f"bereed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("mjau")

    def description(self):
        super().description()

        print(f"Color: {self.color}")

animal = Animal("palidhje")
animal.sound()
animal.description()

dog = Dog("rex", "palidhje")
dog.sound()
dog.description()

cat = Cat("mjau","black")
cat.sound()
cat.description()




