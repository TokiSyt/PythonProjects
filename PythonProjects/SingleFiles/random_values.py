import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second


dice = Dice()
print(dice.roll())

# for i in range(3):
#    print(random.randint(10, 20))

# members = ['John', 'Toki', 'Tina', 'Bebi']
# print(random.choice(members))
