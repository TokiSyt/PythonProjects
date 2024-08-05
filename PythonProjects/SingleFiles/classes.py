class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}!')


toki = Person("Toki Turcek")
toki.talk()

bob = Person("Bob Kurwa")
bob.talk()