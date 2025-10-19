from random import randint
ask_for_try_again = "yes"
range = int(input("What range do you want it to be? (0, your number)"))
random_number = randint(0, range)
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
