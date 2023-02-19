kms = 0.0002777778
kmh = 3600
user_choice = input("Write h for KM/H to KM/S conversion\nWrite s for KM/S to KM/H conversion \n                      Type here >>> ")
if user_choice == "h":
    user_input = input("\n\nKM/H >>>")
    try:
        print(f"{kms * float(user_input)} KM/S")
    except ValueError:
        print("Bad input. use numeric characters")
elif user_choice == "s":
    user_input = input("\n\nKM/S >>>")
    try:
        print(f"{kmh*float(user_input)} KM/H")
    except ValueError:
        print("Bad input. use numeric characters")
else:
    print("Incorrect input")
