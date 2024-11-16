import random
import time


def num_generator():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    total_num = str(num1) + str(num2) + str(num3) + str(num4)

    print(total_num)
    time.sleep(2)
    print()
    print()
    print()
    answer = input()
    if answer == total_num:
        print("correct")
        time.sleep(2)
    else:
        print("wrong")
        time.sleep(2)


while True:
    num_generator()
