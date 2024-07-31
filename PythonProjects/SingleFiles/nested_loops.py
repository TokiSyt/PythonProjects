# for x in range(4):
#    for y in range(3):
#        print(f"({x}, {y})")

xs = [1, 1, 1, 1, 5]

for x_count in xs:
    line = ''
    for value in range(x_count):
        line += 'x'
    print(line)