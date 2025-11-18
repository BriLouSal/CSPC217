



list_of_num = [x for x in range(1, 101)]



def FizzBuzz(list_numbers: list):
    new_list = []

    for i in list_numbers:
        if i % 3 == 0 and i % 5 == 0:
            new_list.append("FizzBuzz")
        elif i % 3 == 0:
            new_list.append("Fizz")
        elif i % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(i)
    return new_list


print(FizzBuzz(list_of_num))