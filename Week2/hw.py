from random import randint
ask_for_try_again = "yes"
lowerbound = int(input("What range do you want it to be? (pls make it small)"))
upperbound = int(input("What range do you want it to be? (pls make it bigger than last number)"))
random_number = randint(lowerbound, upperbound)
while ask_for_try_again == "yes":
    guess = int(input("What is the number??"))
    if guess == random_number:
        print("YOU WIN!!!")
        ask_for_try_again = "no"
    else:
        print("YOU LOSE :(")
        ask_for_try_again = str(input("Do you want to try again? (yes or no)"))
        if ask_for_try_again == "yes":
            ask_for_try_again = "yes"
        else:
            ask_for_try_again = "no"
