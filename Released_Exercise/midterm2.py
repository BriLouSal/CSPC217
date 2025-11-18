

# for i in range(0,4):
#     print(i)


# 2d Array list (Nested loop tricky)
for j in range(0, 4):
    for i in range(0,3):
        print(i,j)




# ---- FUNCTION ---- #


def greet(name, greeting="Hello"):  # def keyword, function name, parameters
    """This function greets a person.""" # Docstring (part of the body)
    message = f"{greeting}, {name}!"  # Function body statements
    return message # return statement


def main():

    result = greet("Alice")
    print(result) # Output: Hello, Alice!

    another_result = greet("Bob", "Hi")
    print(another_result) # Output: Hi, Bob!

# We may see something such as main() to call of our functions which is greater practice according to Dr Helen
main()

# Argument v.s. Parameters (Parameters we can hint the Value such as def function_name(num: int))
# Parameters are the named variables listed in the function's definition. They act as placeholders for the values that will be passed into the function when it is called. Parameters define the type and number of inputs a function expects. 
#  Arguments are the actual values that are passed to the function when it is invoked or called. These values are assigned to the corresponding parameters within the function's scope.


# Type hint

def  add (a: int, b: int) -> int: # converts into int
    return a + b



print(add('2', '3'))


# But the first parameter can be made optional?
# a=“XXX”
# can you quickly remind me what happens when rows and columns are not all the same in a 2D list?





