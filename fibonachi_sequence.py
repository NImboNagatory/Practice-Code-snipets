while True:
    usr_input = input("Input how many digits of fibonacci sequence you want to see >>> ")
    if usr_input.isnumeric():
        usr_input = int(usr_input)
        break
    else:
        print("bad input!")


def fibon(inputed_int):
    output = ""
    last_fibo = 0
    fibo = 1
    for char in range(1, inputed_int + 1):
        last_fibo += fibo
        fibo = last_fibo - fibo
        output += f"{char}---{last_fibo}\n"
    return output


def golden(inputed_int):
    output = ""
    golden_r = inputed_int
    for char in range(1, inputed_int + 1):
        golden_r = (1 / golden_r) + 1
        output += f"{char}. {round(golden_r, 3)}\n"
    return output


print(f"------------------------\nFibonacci sequence\n{fibon(usr_input)}\n-----------------------------")

print(f"------------------------\nGolden ratio\n{golden(usr_input)}\n-----------------------------")
