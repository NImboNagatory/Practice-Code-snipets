from math import sqrt

a = float(input("Input 'x^2' coefficient of equation >>>"))
b = float(input("Input 'x' coefficient of equation >>>"))
c = float(input("Input coefficient of equation >>>"))

print(- 4 * (a * c))

try:
    root = sqrt((b ** 2) - 4 * (a * c))
    x1 = ((-b - root) / a + a)
    x2 = ((-b + root) / a + a)

    print(f"X1 = {x1}")
    print(f"X2 = {x2}")
except ValueError:
    print('Negative Discriminant')


