import random

text = ""
rand1 = random.randint(10, 20)
rand2 = random.randint(0, rand1)
while True:
    rand3 = random.randint(1, rand1)
    if rand3 != rand2:
        break
rand4 = random.randint(1, 3)
guard_val = 0
rand5 = 0
rand6 = 0
rand7 = 0
while guard_val <= rand4:
    guard_val += 1
    if guard_val == 1:
        loop_true = 1
        while loop_true == 1:
            rand5 = random.randint(0, rand1)
            if rand5 != rand2 and rand5 != rand3:
                loop_true = 0
    if guard_val == 2:
        loop_true = 1
        while loop_true == 1:
            rand6 = random.randint(0, rand1)
            if rand6 != rand2 and rand6 != rand3 and rand6 != rand5:
                loop_true = 0
    if guard_val == 3:
        loop_true = 1
        while loop_true == 1:
            rand7 = random.randint(0, rand1)
            if rand7 != rand2 and rand7 != rand3 and rand7 != rand5 and rand7 != rand6:
                loop_true = 0

for item in range(0, rand1):
    if item == rand2-1:
        text += "$"
    elif item == rand3-1:
        text += "T"
    elif item == rand5 or item == rand6 or item == rand7:
        text += "G"
    else:
        text += "x"
print(text)


command = text
iterate = 0
thief = 0
money = 0
item_list = []
for item in command:
    iterate += 1
    if item == "T":
        thief = iterate - 1
    if item == "$":
        money = iterate - 1
iterate = 0
for item in command:
    iterate += 1
    if thief > money:
        if (iterate >= money+1) and (iterate <= thief+1):
            item_list.append(item)
    if money > thief:
        if (iterate <= money+1) and (iterate >= thief+1):
            item_list.append(item)
iterate = 0
for item in item_list:
    iterate += 1
    if item == "G":
        print("quiet")
        break
    if iterate == len(item_list):
        print("ALARM")
