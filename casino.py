import random
import time

coins = 1000
win1 = -10
win2 = 100
win3 = 1000
win4 = 10000
val1 = 0
val2 = 0
val3 = 0
play = True

print('Welcome to Casino\n')


def format_slots(val1, val2, val3, iter, val):
    chars = ["#", "*", "@", "$", "&", "+", "∆", "=", "×", "%"]
    time.sleep(.2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print('_______')
    if iter == 1 and val < 2:
        nums='|{0}|{1}|{2}|_|'.format(chars[val1], chars[val2],chars[val3])
        print(nums)
        print('_______ ')
    if iter == 1 and val >= 2:
        nums='|{0}|{1}|{2}|_'.format(chars[val1], chars[val2],chars[val3])
        print(nums)
        print('_______ |')
    if iter != 1:
        nums='|{0}|{1}|{2}|_|'.format(chars[val1], chars[val2],chars[val3])
        print(nums)
        print('_______')


def game_slots(coins):
    iter = 0
    rand1 = random.randint(0, 9)
    rand2 = random.randint(0, 9)
    rand3 = random.randint(0, 9)
    while iter < 6:
        iter += 1
        if iter == 1:
            for i in range(0, 10):
                val1 = i
                val2 = i
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
        if iter == 2:
            for i in range(0, rand1+1):
                val1 = i
                val2 = i
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
            for i in range(rand1, 10):
                val2 = i
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
        if iter == 3:
            for i in range(0, rand2+1):
                val2 = i
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
            for i in range(rand2, 10):
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
        if iter == 4:
            for i in range(0, rand3+1):
                val3 = i
                format_slots(val1, val2, val3, iter, val1)
    if rand1 == rand2 and rand1 == rand3:
        print('\nYOU WIN')
        print("\ngained 1000 coins\n")
        coins += win3
    elif rand1 == rand2 or rand2 == rand3 or rand1 == rand3:
        print('\nYOU WIN')
        print("\ngained 100 coins\n")
        coins += win2
    else:
        print('\nYOU LOSE')
        print("\nlost 10 coins\n")
        coins = coins + win1
    return(coins)


def game_scratch(coins):
    guesses = 4
    list = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)']
    chars = [" # ", " * ", " @ ", " $ ", " & ", " + ", " ∆ ", " = ", " × ", " % "]
    rand_list = []
    while guesses > -1:
        print("\n\n\n\n\n")
        guesses = guesses - 1
        for i in range(0, 3):
            text1 = '|{0}| |{1}| |{2}|'.format(list[3 * i], list[3 * i + 1], list[3 * i + 2])
            text2 = '_____ _____ _____ '
            print(text2)
            print(text1)
            print(text2)
        if guesses > -1:
            rand1 = random.randint(0, 9)
            command = input('\nyou have ' + str(guesses + 1) + ' scratches left  ')
            list[int(command)-1] = chars[int(rand1)-1]
            rand_list.append(rand1)
    val1 = rand_list[0]
    val2 = rand_list[1]
    val3 = rand_list[2]
    val4 = rand_list[3]
    if val1 == val2 and val1 == val3 and val1 == val4:
        coins += win4
        print('\nYOU WIN')
        print("\ngained 10000 coins\n")
    elif (val1 == val2 and val1 == val3) or (val1 == val2 and val1 == val4) or (val2 == val3 and val2 == val4) or (val1 == val3 and val1 == val4):
        coins += win3
        print('\nYOU WIN')
        print("\ngained 1000 coins\n")
    elif (val1 == val2) or (val1 == val3) or (val1 == val4) or (val2 == val3) or (val2 == val4) or (val3 == val4):
        coins += win2
        print('\nYOU WIN')
        print("\ngained 100 coins\n")
    else:
        coins = coins - 10
        print('\nYOU LOSE')
        print("\nlost 10 coins\n")
    return(coins)


#def game_blackjack():
#    suit = ["♢", "♥", "♤", "♧"]
#    vals = [" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10", " J", " Q", " K", " A"]
#    rand1 = random.randint(0,4)
#    rand2 = random.randint(0,14)
#    text1 = "_________:
#    text2 = "|       |"
#    text3 = "|_______|"
#    text4 = "|  {0}{1}  |".format(suit[rand1], )
#    print(text1)
#    print(text2)
#    print(text2)
#    print(text4)
#    print(text2)
#    print(text3)

while play == True:
    command = input('(h)elp\n(s)lots\n(b)lackjack\ns(c)ratch\n(e)xit\n')
    if command == 'h':
        input("""


Description:
A casino game based on chance
You start with 1000 coins, play games to earn prizes

Slots:
1 same  |   -10
2 same  |   +100
3 same  |   +1000

Blackjack:


Scratch:
1 same  |   -10
2 same  |   +100
3 same  |   +1000
4 same  |   +10000

Developed by:
Peter Babych

(press enter)
""")
    if command == 's' or command == '':
        command = input('\nplaying slots\nyou have ' + str(coins) + ' coins \n\n(b)ack \n(c)ontinue\n')
        if command != 'b':
            coins = game_slots(coins)
    #if command == 'b':
    if command == 'c':
        command = input('\nplaying scratch\nyou have ' + str(coins) + ' coins \n\n(b)ack \n(c)ontinue\n')
        if command != 'b':
            coins = game_scratch(coins)
    if command == 'e':
        play = False


#_________
#|       |
#|       |
#|  {0}{1}  | ♢♥♤♧
#|       |
#|_______|
