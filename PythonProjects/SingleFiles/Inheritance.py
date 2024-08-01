class Mammal:
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Bark...")



class Cat(Mammal):
    def meow(self):
        print("Meow...")


cat1 = Cat()
cat1.meow()