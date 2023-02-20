while True:
    try:
        usr_input = int(input("Generate hexadecimal and binary up to this decimal number >>> "))
        break
    except ValueError:
        print("Bad input!")


def decimaltobinary(n):
    return bin(n)


conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}


def decimaltohexadecimal(decimal):
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


print("Using slices we will show you the portion of the list")
start_inp = int(input("Start at >>> "))
stop_inp = int(input("Stop at >>> "))
print(f"Decimal Values from {start_inp} to {stop_inp}")
for char in range(start_inp, stop_inp):
    print(char)
print(f"Binary values from {start_inp} to {stop_inp}")
for char in range(start_inp, stop_inp):
    print(decimaltobinary(char))
print(f"Hexadecimal values from {start_inp} to {stop_inp}")
for char in range(start_inp, stop_inp):
    print(decimaltohexadecimal(char))

cont = input(f"Press enter to continue to see all values from 1 to {usr_input}")

print("DECIMAL----HEXADECIMAL----Binary")
for char in range(1, usr_input+1):
    print(f"{char}----{decimaltohexadecimal(char)}----{decimaltobinary(char)}")
