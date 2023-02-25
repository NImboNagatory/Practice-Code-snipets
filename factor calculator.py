while True:
    try:
        usr_input = int(input("Input a number you want The factor of >>> "))
        break
    except ValueError:
        print("Bad Input!")
factors = []
for char in range(1, usr_input + 1):
    if usr_input % char == 0:
        factors.append(char)
print(factors)
