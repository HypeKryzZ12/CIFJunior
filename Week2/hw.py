from random import randint
random_number = randint(0, 100)
guess = int(input("What is the number??"))
if guess == random_number:
    print("YOU WIN!!!")
else:
    print("YOU LOSE :(")
