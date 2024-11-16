import random
import time
from timeit import default_timer

start = default_timer()

HP = 1100
HP_max = 1100
attack = 2200
defence = 1000
regen_pot_count = 0
candy = 600

witch_B_dead = 0
witch_U_dead = 0
witch_G_dead = 0


def lose():
    print("""your stats are now:
HP =  100
max HP =  100
attack =  10
defence =  10
regen =  0
candies =  0""")


def win():
    duration = default_timer() - start
    print("\n\n\n\n\n\n\n\n")
    print("congratulations you beat the game in " + str(int((duration/60)//1)) + " minutes")
    time.sleep(5)


def fight(c, a, d, h, h_max, r, name, lvl, e_a, e_d, e_h, e_r):
    w = 0
    e_hmax = e_h
    run = 1
    while run:
        attack_pass = 0
        print()
        print("___fighting " + name + "___")
        print("enemy HP  [" + "#"*(int(((e_h/e_hmax)*10)//1)) + " "*(10-(int(((e_h/e_hmax)*10)//1))) + "]  " + str(e_h))
        print("player HP [" + "#"*(int(((h/h_max)*10)//1)) + " "*(10-(int(((h/h_max)*10)//1))) + "]  " + str(h))
        print()
        print("(f)ight")
        print("(r)egen")
        print("r(u)n (costs", lvl, "candies)")
        command = input()
        if command == "f":
            if a - e_d >= 0:
                e_h -= a - e_d
                print("you dealt " + str(a - e_d) + " damage")
            if a - e_d < 0:
                print("you dealt 0 damage")

            if e_h <= 0:
                print("enemy HP  [          ]  0")
                print("you killed the enemy")
                if e_r == 0:
                    rng4 = random.randint(1, lvl)
                    c += rng4
                    print("it dropped " + str(rng4) + " candies")
                    print()
                    w = 1
                    break
                if e_r == 1:
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print("I'M TIRED OF ALL THIS FIGHTING")
                    time.sleep(3)
                    print("I GUESS YOU COULD SAY THAT YOU WIN")
                    time.sleep(3)
                    print("the Elevated One vanishes")
                    time.sleep(4)
                    win()
                    w = 1
                    break
                if e_r == 2:
                    e_r -= 1
                    attack_pass = 1
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print("LETS MAKE THIS FUN SHALL WE")
                    time.sleep(3)
                    print("the Elevalted One regenerated 12 HP")
                    time.sleep(4)
                    print("the Elevated One's defence is now " + str(a-1))
                    time.sleep(4)
                    print("the Elevated One's attack is now " + str(h_max+d-1))
                    time.sleep(4)
                    print()
                    print()
                    print()
                    e_h = 12
                    e_a = h_max+d-1
                    e_d = a-1
                if e_r == 3:
                    e_r -= 1
                    attack_pass = 1
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print("I CAN DO THIS ALL DAY")
                    time.sleep(3)
                    print("the Elevalted One regenerated 1000 HP")
                    time.sleep(4)
                    print("the Elevated One gained 600 defence")
                    time.sleep(4)
                    print("the Elevated One gained 600 attack")
                    time.sleep(4)
                    print()
                    print()
                    print()
                    e_h = 1000
                    e_a += 600
                    e_d += 600
                if e_r == 4:
                    e_r -= 1
                    attack_pass = 1
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print("YOU REALLY THINK YOU COULD KILL ME?")
                    time.sleep(2)
                    print("IT WOULD BE UNFAIR IF ONLY YOU COULD HEAL")
                    time.sleep(2)
                    print("the Elevalted One regenerated 2000 HP")
                    time.sleep(4)
                    print("the Elevated One gained 200 defence")
                    time.sleep(4)
                    print("the Elevated One gained 200 attack")
                    time.sleep(4)
                    print()
                    print()
                    print()
                    e_h = 2000
                    e_a += 200
                    e_d += 200

            if e_a - d >= 0 and attack_pass == 0:
                h -= e_a - d
                print("enemy dealt " + str(e_a - d) + " damage")
            if e_a - d < 0 and attack_pass == 0:
                print("enemy dealt 0 damage")

            if h <= 0:
                print("player HP [          ]  0")
                print("you died")
                print()
                lose()
                print()
                h = HP
                h_max = HP_max
                a = attack
                d = defence
                r = regen_pot_count
                c = candy
                break
        if command == "r":
            regen = 1
            while regen:
                try:
                    print()
                    print("how many regen potions do you want to use (you have " + str(r) + ")")
                    command = int(input())
                    if command > r:
                        print("you don't have that many regen potions")
                    else:
                        r -= command
                        h += 100 * command
                        print("you used " + str(command) + " regen potions (" + str(r) + " potions left)")
                        if h > h_max:
                            h = h_max
                        print("regenerated " + str(100 * command) + " HP")
                        print("you now have " + str(h) + " HP (max " + str(h_max) + ")")
                        regen = 0
                except:
                    print("invalid number")
        if command == "u":
            print("you run from the monster")
            print("you lost " + str(lvl) + " candies")
            c -= lvl
            run = 0

    return c, a, d, h, h_max, r, w


def search(c, a, d, h, h_max, r):
    rng1 = random.randint(0, 5)
    if rng1 == 1:
        rng2 = random.randint(1, 4)
        print()
        print("you searched the forest and found", rng2, "candy(s)")
        c += rng2
    if rng1 != 1:
        rng3 = random.randint(1, 10)
        print()
        print("you stumbled across a level", rng3, "monster")
        while True:
            print("""(f)ight
(r)un""")
            command = input()
            if command == "f":
                c, a, d, h, h_max, r, w = fight(c, a, d, h, h_max, r, "lvl " + str(rng3) + " monster", rng3, 10*rng3, 2*rng3, 15*rng3, 0)
                break
            if command == "r":
                print("you ran from the monster")
                break

    return c, a, d, h, h_max, r


def view(c, a, d, h, h_max, r):
    print("your stats are:")
    print("HP = ", h)
    print("max HP = ", h_max)
    print("attack = ", a)
    print("defence = ", d)
    print("regen = ", r)
    print("candies = ", c)


def witch(c, a, d, h, h_max, r, b, u, g):
    #b
    #witch_HP = 400
    #witch_attack = 450
    #witch_defence = 40
    #u
    #witch_HP = 200
    #witch_attack = 600
    #witch_defence = 60
    #g
    #witch_HP = 300
    #witch_attack = 300
    #witch_defence = 80
    while True:
        print("choose a witch to fight")
        print("(B)aba-Yaga (high HP, low defence)" + "  [defeated]"*b)
        print("(U)rsula    (low HP, high attack)" + "   [defeated]"*u)
        print("(G)linda    (high defence)" + "          [defeated]"*g)
        print("(l)eave")
        command = input()
        if command.lower() == "b":
            c, a, d, h, h_max, r, w = fight(c, a, d, h, h_max, r, "Baba-Yaga", 50, 450, 40, 400, 0)
            if w == 1:
                b = 1
        if command.lower() == "u":
            c, a, d, h, h_max, r, w = fight(c, a, d, h, h_max, r, "Ursula", 50, 600, 60, 200, 0)
            if w == 1:
                u = 1
        if command.lower() == "g":
            c, a, d, h, h_max, r, w = fight(c, a, d, h, h_max, r, "Glinda", 50, 300, 80, 300, 0)
            if w == 1:
                g = 1
        if command == "l":
            break
    return c, a, d, h, h_max, r, b, u, g


def elevated(c, a, d, h, h_max, r):
    #elevated_HP = 4000
    #elevated_attack = 1000
    #elevated_defence = 800
    print("You are about to summon the Elevated One")
    print("Are you sure")
    print("(Y/N)")
    command = input()
    if command.lower() == "y":
        time.sleep(1)
        print()
        time.sleep(1)
        print()
        time.sleep(1)
        print("a voice booms:")
        time.sleep(2)
        print("WHO DARES SUMMON THE ELEVATED ONE")
        time.sleep(2)
        print("YOU?")
        time.sleep(2)
        print("FOOLISH MORTAL")
        time.sleep(2)
        print("I WILL DESTROY YOU")
        time.sleep(2)
        c, a, d, h, h_max, r, w = fight(c, a, d, h, h_max, r, "Elevated One", 0, 1000, 800, 4000, 4)
    return c, a, d, h, h_max, r, w


def main(c, a, d, h, h_max, r, b, u, g):
    win = 0
    while not win:
        command = input("""
(s)earch forest
(v)iew stats
(e)nter store
(f)ight witch
(c)hallenge Elevated One
""")
        if command == "s":
            c, a, d, h, h_max, r = search(c, a, d, h, h_max, r)
        if command == "v":
            view(c, a, d, h, h_max, r)
        if command == "e":
            leave_store = 0
            while leave_store == 0:
                print("you have ", c, "candies")
                print("upgrade (a)ttack   (5 candy)")
                print("upgrade (d)efence   (5 candy)")
                print("upgrade (h)ealth   (5 candy)")
                print("buy (r)egen   (3 candy)")
                print("(l)eave store")
                command = input("")
                p = command[0]
                q = command[1:]
                if q == "":
                    q = 1
                q = int(q)
                if p == "a" and c >= 5*q:
                    print("you upgraded your attack")
                    a += 5*q
                    c += -5*q
                    print("you attack is now ", a)
                    print("you now have", c, "candies remaining")
                    print(" ")
                    command = ""
                elif p == "a" and c < 5*q:
                    print("you do not have enough candies")
                    print("")
                if p == "d" and c >= 5*q:
                    print("you upgraded your defence")
                    d += 5*q
                    c += -5*q
                    print("you defence is now ", d)
                    print("you now have", c, "candies remaining")
                    print(" ")
                    command = ""
                elif p == "d" and c < 5*q:
                    print("you do not have enough candies")
                    print("")
                if p == "h" and c >= 5*q:
                    print("you upgraded your health")
                    h += 50*q
                    h_max += 50*q
                    c += -5*q
                    print("your health is now ", h)
                    print("your max HP is now ", h_max)
                    print("you now have", c, "candies remaining")
                    print("")
                    command = ""
                elif p == "h" and c < 5*q:
                    print("you do not have enough candies")
                    print("")
                if p == "r" and c >= 3*q:
                    print("you bought regen")
                    r += q
                    c += -3*q
                    print("you regen count is now ", r)
                    print("you now have", c, "candies remaining")
                    print(" ")
                    command = ""
                elif p == "r" and c < 3*q:
                    print("you do not have enough candies")
                    print("")
                if p == "l":
                    leave_store = 1
                    print("you left the store")
                    print(" ")
        if command == "f":
            c, a, d, h, h_max, r, b, u, g = witch(c, a, d, h, h_max, r, b, u, g)
        if command == "c":
            if b + u + g == 3:
                c, a, d, h, h_max, r, w = elevated(c, a, d, h, h_max, r)
                if w == 1:
                    win = 1
            else:
                print("you need to defeat all three witches first")


main(candy, attack, defence, HP, HP_max, regen_pot_count, witch_B_dead, witch_U_dead, witch_G_dead)
