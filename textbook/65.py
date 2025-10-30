
# Exercise 65:Temperature Conversion Table
# (22 Lines)
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the Internet.


def fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9 


user = float(input("Choose a temperture number in Celc or Farenheight (Choose a number): "))

ask_user = input("Is it in C or F: ").capitalize()


if ask_user == "C":
    print(f"This tempeture in F is {fahrenheit(user)}")
if ask_user == "F":
    print(f"This tempeture in C is {fahrenheit(user)}")
else:
    print("Does not exist! ")
# (0°C × 9/5) + 32 = 32°F



