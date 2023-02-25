usr_input = input("Input a list of numbers separated by space >>> ")

data = usr_input.split()

odd = []
even = []

for char in data:
    if char.isnumeric():
        if int(char) % 2 == 0:
            even.append(char)
        else:
            odd.append(char)


print(f"Odd: {odd}")
print(f"Even: {even}")
