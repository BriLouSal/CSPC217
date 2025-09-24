# x = int(input("What is your number: "))
# y = int(input("What is your second number: "))
#
# error_check = False
# # Syntax Error, this is not how it works, and you cannot have a single elif. Else if
# if x > 0:
#     if y > 0:
#         print("Both are positive")
#     elif y <= 0:
#         print("X is positive and Y is Negative")
# else:
#     if y < 0:
#         print("X is negative, and Y is Positive")
#     elif y < 0:
#         print("Both are Negative")


#  Syntax error
# if 5 >3
#     "Sucker"

# Runtime Error: (We can prevent this with Error Handling by using Try and Except)


# The Province x Age question would be a logic error, you would want to put the Age inside
# if statement, and you don't have other provinces that would have legal age of 21 to buy alcohol


province = input("Enter your province or territory: ").title()
age = int(input("Enter your Age: "))

# if province == "Alberta" or province == "Manitoba" or province == "Quebec":
#     if age >= 18:
#         print("Your are of legal age to buy beer")
#     else:
#         print("You're not of legal age to buy beer")
# else:
#     if age >= 21:
#         print("You're of Legal Age to buy beer")
#     else:
#         print("You cannot buy beer, as you're not of age")


if province == ("Alberta" or province == "Manitoba" or province == "Quebec") and age >= 18:
        print("Your are of legal age to buy beer")

else:
    if age >= 21:
        print("You're of Legal Age to buy beer")
    else:
        print("You cannot buy beer, as you're not of age")



#  https://docs.google.com/document/d/1oQwMvwTu9dWqqizc8CMeyv0PcFiWbaRZ_Rk1zW_NKNY/edit?tab=t.0






