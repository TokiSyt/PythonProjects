'''
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day\nDrink plenty of water")
elif is_cold:
    print("It's a cold day\nWear warm clothes")
else:
    print("It's a lovely day\nEnjoy your day")
'''

house_price = 1000000
buyer_creditIsGood = True

if buyer_creditIsGood:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Down payment: ${down_payment}")