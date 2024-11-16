import random

wins = 0
total_list = ""
for item in range(0, 100001):
    skip = 0
    val1 = random.randint(1, 8)
    val2 = random.randint(1, 8)
    val_total = val1 + val2
    total = item
    total_list = total_list + "(" + str(val1) + "," + str(val2) + ")" + ", "
    if val1 == 8:
        wins += 1
        skip = 1
    elif skip == 0 and val2 == 8:
        wins += 1
    elif skip == 0 and val1 == 7 and val2 != 1:
        wins += 1
    elif skip == 0 and val2 == 7 and val1 != 1:
        wins += 1
print(total_list)
print(wins)
print(total)
print(wins / total)


