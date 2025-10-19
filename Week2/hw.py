from random import randint
range = int(input("What range do you want it to be? (0, your number)"))
random_number = randint(0, range)
guess = int(input("What is the number??"))
if guess == random_number:
    print("YOU WIN!!!")
else:
    print("YOU LOSE :(")
