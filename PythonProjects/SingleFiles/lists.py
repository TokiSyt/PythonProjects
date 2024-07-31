# names = ['Toki', 'Tina', 'Bebi', 'Macaco', 'Salvas']
# names[0] = 'Tokei'
# print(names[2:])
# print(names)

list = [12, 3, 4411, 62, 25, 2352]
biggest_number = list[0]

for numbers in list:
    if biggest_number < numbers:
        biggest_number = numbers
print(biggest_number)
