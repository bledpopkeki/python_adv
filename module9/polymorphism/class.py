class Dog:

    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes a sound:Woof!")


class Cat:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound:mjau!")


class bird:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound:ciu!")


dog=Dog("badi")
cat=Cat("visker")
bird=Bird("tviti")

for animal in (dog,cat,bird):
    animal.sound()