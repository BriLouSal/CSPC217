# Lec 20a - Files







#W We want traversing thoruhg the loops, and it's more into function, and it will go till lists and dictionary

# Step 1: Locate the files, know which file to open

# Step 2: Open the files, 
file_object = open('brian.txt', mode='w')


input_user = input("What do you want? ")
# Step 3: Reading the data, and parsing it by sorting it by negative, or higher returns, etc.


with open('brian.txt', mode='w') as file:
    file.write(input_user)