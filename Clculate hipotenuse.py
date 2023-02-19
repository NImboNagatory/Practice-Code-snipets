from math import sqrt

usr_in1 = int(input("Input first leg of Triangle >>>"))
usr_in2 = int(input("Input second leg of Triangle >>>"))


def calc_hipot(lg1, lg2):
    try:
        hipot = sqrt((lg1 * lg1) + (lg2 * lg2))
        s = (lg1+lg2+hipot)/2
        area = sqrt(s*((s-lg1)*(s-lg2)*(s-hipot)))
        print(f"Triangle with legs of {lg1} and {lg2} the hypotenuse is {round(hipot)}")
        print(f"Triangle with legs of {lg1} and {lg2} the area is {round(area)}")
    except TypeError:
        print("Bad input")


calc_hipot(usr_in1, usr_in2)
