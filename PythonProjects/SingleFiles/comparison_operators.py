'''temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It is not a hot day")'''

# different is !=

name = input("Choose your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good!")