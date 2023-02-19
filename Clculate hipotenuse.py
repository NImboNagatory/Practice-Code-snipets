from math import sqrt

usr_in1 = input("Input first leg of Triangle >>>")
usr_in2 = input("Input second leg of Triangle >>>")


def calc_hipot(lg1, lg2):
    try:
        lg1 = float(lg1)
        lg2 = float(lg2)
        hipot = sqrt((lg1 * lg1) + (lg2 * lg2))
        s = (lg1+lg2+hipot)/2
        area = sqrt(s*((s-lg1)*(s-lg2)*(s-hipot)))
        print(f"Triangle with legs of {lg1} and {lg2} the hypotenuse is {round(hipot, 2)}")
        print(f"Triangle with legs of {lg1} and {lg2} the area is {round(area, 2)}")
    except ValueError:
        print("Bad input")


calc_hipot(usr_in1, usr_in2)
