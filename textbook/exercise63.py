# Exercise 63:Average


# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.


def average(num_list: list) -> float:
    return sum(num_list) / len(num_list)


user = float(input("Choose a num: "))
list_of_numbers = []

while user != 0:
    if user == 0:
        break
    else:
        list_of_numbers.append(user)
        user = float(input("Choose a num: "))
print(average(list_of_numbers))
