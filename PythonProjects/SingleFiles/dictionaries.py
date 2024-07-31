'''customer = {
    "name": "Tokei",
    "age": 20,
    "is_verified": True
}

customer["name"] = "Toki"
customer["birthdate"] = "2004/05"

print(customer)
'''

numbers_requested = input('Numbers: ')
result = ''

converter = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

for number in numbers_requested:
    result += converter.get(number, "Do not have this number") + ' '

print(result)