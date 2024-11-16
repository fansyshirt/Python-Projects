import random

random_number = random.randint(1, 101)
command = " "
max_guesses = 6  # 7 guesses
guessed = 0

for guesses in range(0, 7):
    print(" ")
    command = int(input("take a guess "))
    print(" ")
    if command > random_number:
        print("lower ")
        command = 0
    elif command < random_number and command != 0:
        print("higher ")
        command = 0
    elif command == random_number:
        print("you guessed it ")
        print("thanks for playing ")
        guessed = 1
        break

if guessed == 0:
    print("you ran out of guesses ")
