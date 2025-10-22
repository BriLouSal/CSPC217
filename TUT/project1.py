# foo = "10C"
# suit = foo[-1]
# rank = foo[:-1]
# print(f”The rank is {rank} and the suit is {suit}.”)


# foo = "JC"
# suit = foo[-1] # Output is C
# rank = foo[:-1] # Output is 10

# The	user	will
# enter	the	rank (either 2-10 or J for Jack, Q for Queen, K for King, A for Ace
# What we can do is separate the suit, check if the suit is 1 < suit < 11, or suit has
#  J,Q,K,A. Else we can exit the code.

# We need to create a sum_of_points value in order to count the values of each card inputted
# So this project is mainly focused on branch if-else statement, as the lecture also reminded me
# that a value can exist when an if-statement is satisfied.

# Ask user for their first card
ask_card_one = input("Card 1: ")
# Use string slicing to obtain suit, and rank
suit = ask_card_one[-1]

rank = ask_card_one[:-1]

print(rank, suit)

# These are constant variable to ensure that our code is readable, and doesn't follow magic number rule
MIN_RANK = 1
MAX_RANK = 11

point_value = 0
# I have an idea to see if the number is a integer or not, so it's optimized that we ensure if statements
# Check is rank is string and similar
# And we can do a nested if statement to check if suit does exists, else it would cancel the code

if (rank == "J" or rank == "Q" or rank == "J" or rank == "A"):
    if suit == "C" or suit == "H" or suit == "D" or suit == "S":
        if rank == "J" or rank == "Q" or rank == "K":
            point_value = 10
        elif rank == "A":
            point_value = 11

        print(f"Card1: {rank}{suit}")

        print(point_value)

        ask_card_two = input("Card 2: ")
        suit_1 = ask_card_two[-1]
        rank_1 = ask_card_two[:-1]

        if ask_card_two == ask_card_one:
            print(f"There can't be two {ask_card_two} in the same hand. You're playing with a fake deck!")

        elif rank_1[0] == '1' or rank_1[0] == '2' or rank_1[0] == '3' or rank_1[0] == '4' or rank_1[0] == '5' or rank_1[
            0] == '6' or rank_1[0] == '7' or rank_1[0] == '8' or rank_1[0] == '9':
            if suit_1 == "C" or suit_1 == "H" or suit_1 == "D" or suit_1 == "S":
                if rank == "J" or rank == "Q" or rank == "K":
                    point_value = 10
                elif rank == "A":
                    point_value = 11


                else:
                    rank_1 = int(rank_1)

                    point_value = rank_1
            else:
                print(f"Invalid suit {suit}. Must be H, D, C, or S")
                exit()
        else:
            print(f"{rank}{suit} Does not exist")

    else:
        print(f"Invalid suit {suit}. Must be H, D, C, or S")

# Check if rank is equals to a digit

# This will check if the digit is 1 -> 9. We don't need to worry as adding 9b ensure that 9 is only taken for consideration

# Check if the string space is a digit, such as that it could be 1bb. And say it's a rank (which is not ok!)

elif (rank[0] or rank[1]== '1') or (rank[0] or rank[1] == '2') or (rank[0] or rank[1] == '3') or (rank[0]  or rank[1]== '4') or (rank[0] or rank[1] == '5') or rank[0] == '6' or rank[
    0] == '7' or rank[0] == '8' or rank[0] == '9':

    if suit == "C" or suit == "H" or suit == "D" or suit == "S":

        print(f"{rank}{suit}")

        rank = int(rank)

        if MIN_RANK < rank < MAX_RANK:
            print("nil")
            exit()


        else:
            point_value = rank

            ask_card_two = input("Card 2: ")

            suit_1 = ask_card_two[-1]

            rank_1 = ask_card_two[:-1]

            if rank_1 == "J" or rank_1 == "Q" or rank_1 == "J" or rank_1 == "A":

                if suit_1 == "C" or suit_1 == "H" or suit_1 == "D" or suit_1 == "S":

                    if rank == "J" or rank == "Q" or rank == "K":
                        point_value = 10

                    elif rank == "A":
                        point_value = 11

                    else:
                        if suit_1 != suit:
                            point_value = rank

                        else:
                            point_value = point_value + int(rank_1)

            elif rank_1[0] == '1' or rank_1[0] == '2' or rank_1[0] == '3' or rank_1[0] == '4' or rank_1[0] == '5' or \
                    rank_1[0] == '6' or rank_1[0] == '7' or rank_1[0] == '8' or rank_1[0] == '9':

                if suit_1 == "C" or suit_1 == "H" or suit_1 == "D" or suit_1 == "S":
                    if rank == "J" or rank == "Q" or rank == "K":
                        point_value = 10
                        print(point_value)
                    elif rank == "A":
                        point_value = 11
                        print(point_value)
                    else:

                        if suit_1 != suit:
                            point_value = rank

                        else:
                            point_value = point_value + int(rank_1)
                            print(point_value)
                
                else:
                    print(f"Invalid suit {suit}. Must be H, D, C, or S")
                    
    else:
        print(f"Invalid suit {suit}. Must be H, D, C, or S")

else:
    print(f"{rank}{suit} Does not exist")
