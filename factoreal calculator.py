try:
    while True:
        usr_input = input("Input the number you want to know factorial of here >>> ")
        if usr_input.isnumeric():
            usr_input = int(usr_input)
            break
        else:
            print("\nOnly numeric characters accepted!\n")
    facto = 1
    for char in range(1, usr_input + 1):
        facto = facto * char
    print(f"factorial of {usr_input} is {facto}")
except ValueError:
    print("Bad Input!")


