usr_name = input("What is your name? >>> ")
while True:
    try:
        usr_grade_count = int(input("How many grades do you want to enter? >>> "))
        break
    except ValueError:
        print("Bad input!")

grades = []
for char in range(usr_grade_count):
    while True:
        try:
            usr_grade = float(input("Enter grade >>>"))
            break
        except ValueError:
            print("Bad input!")
    grades.append(usr_grade)

grades.sort(reverse=True)
print("\n\nGrades From highest to lowest:")
[print(f"               {char}") for char in grades]

print(f"{usr_name}'s grade summery:\n               Total number of grades:{len(grades)}\n               Lowest grade:{min(grades)}\n               Highest grade:{max(grades)}\n               Average:{sum(grades)/len(grades)}")


while True:
    try:
        usr_des_input = float(input("Whats you desired Average grade? >>>"))
        break
    except ValueError:
        print("Bad input")

print(""
      "")