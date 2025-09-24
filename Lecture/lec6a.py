# September 15th


# Three types of error in Programming Endeavours: Runtime (Takes a lot of time to run, catalyzing
# the code to be overwhelmed), Syntax Error (Not following the programming languages rules
# (known as exception; we'll need this later using Try and Except), Module Error (import is not recognized)


# This is an example of module error (Try):
#
# import django.contrib

# We should get ModuleNotFoundError, as we haven't pip installed this library or have the
# qualification to import this (we need to create a django startapp)


# i = 5
#
# # Example of Runtime error
#
#
# num_1 = input("What is your first number: ")
#
# num_2 = input("What is your second number: ")

# THe syntax is correct. However, it would catalyze in a TypeError due to the fact that it's a string
# , and we cannot divide a string lol
#
#
# print(num_1 / num_2)

# Syntax Error:

# Not following the syntax rules of Python, and it would give us a warning

# print("hello)

# Unexpected indentation (This is only necessary if you're using an if-statement)
# print("Hello")
#
# import math as ms
#
# radius = float(input("What is your radius: "))
#
# area_of_circle = round(ms.pi * (radius ** 2), 2)
#
# print(area_of_circle)

# In our exams: We should identify: runtime error, syntax error, logic error; and also fix the errors


#  CONSTANTS: AREA = 2 (example of Python's constant var)

# Javascript:
# const Area  = 2;


# Constants should never be modified throughout your program

# You should never modify it,  EVER!!!

# Applicable use of Constant: USER_OWNER = "Brian". If you're doing a full-stack website, or other projects
# You can use this to never change the owner of the user, or have a variable that you don't wanna change



# Conditionals
#
# first_name = input("What is your name: ")
# amount_of_letters = len(first_name)
#
# print(amount_of_letters)
#
# if amount_of_letters > 5:
#     print("Your name has more than 5 letters ")
# elif amount_of_letters == 5:
#     print("You have exactly 5 letters in your name")
# else:
#     print("Less than 5 letters.")
#
# print("Program ending....")

# using If statements instead of Elif could have a inefficient code, which would catalyze in having
# A longer runtime error : log o(n)^2


# Applicable use of If statements (A Calculator!)


# operator = input("What operation do you want to choose (*, +, **, //, /, -, %: ")
#
# number_one = int(input("What is your first number: "))
#
# number_two = int(input("What is your second number: "))
#
# if operator == "*":
#     result = number_one * number_two
#     print(result)
# elif operator == "+":
#     result = number_one + number_two
#     print(result)
# elif operator == "-":
#     result = number_one - number_two
#     print(result)
# elif operator == "**":
#     result = number_one ** number_two
#     print(result)
# elif operator == "//":
#     result = number_one // number_two
#     print(result)
# elif operator == "%":
#     result = number_one % number_two
#     print(result)
# elif operator == "/":
#     result = number_one / number_two
#     print(result)
# else:
#     print("Please try again")
#






