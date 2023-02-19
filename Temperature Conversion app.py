farenhait = 33.8
kelvin = 274.15

user_input = input("write c for Celsius here >>> ")

try:
    user_input = float(user_input)
    print(f"{round(user_input)} Celsius\n{round(user_input*kelvin)} Kelvin\n{round(user_input+farenhait)} Farenhait")
except ValueError:
    print("Bad input")

