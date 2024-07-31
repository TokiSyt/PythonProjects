Weight = int(input("Weight: "))
kilo_pound = input("(L)bs or (K)g: ")

if kilo_pound.upper() == "K":
    converted = Weight * 2.20
    print(f"You weight {converted} pounds.")
elif kilo_pound.upper() == "L":
    converted = Weight * 0.45
    print(f"You weight {converted} kilos.")
else:
    print("Please insert K or L only.")