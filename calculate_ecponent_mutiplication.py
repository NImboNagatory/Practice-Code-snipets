usr_in = input("Input you number here >>>")


def calc(inputed):
    try:
        inputed = float(inputed)
        output_ecp = ""
        output_mult = ""
        for char in range(1, 11):
            output_mult += f"{inputed} * {char} = {inputed * float(char)}\n"
            output_ecp += f"{inputed} ** {char} = {round(inputed ** char, 3)}\n"

        print(f"multiplication table for {inputed}")
        print(output_mult)
        print(f"component table for {inputed}")
        print(output_ecp)
    except ValueError:
        print("Bad input")

calc(usr_in)
