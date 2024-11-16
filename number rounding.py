num = input("number  ")
decimal = input("decimal value  ")
num_list = []
num_round_list = []

for item in num:
    num_list.append(int(item))
keep_val = int(decimal) * -1
num_list_keep = num_list[0:keep_val]
decider_val = num_list[keep_val]

if decider_val < 5:
    rounding_list = num_list_keep[::]
    rounding_list.reverse()
    rounding_num = 0
    power_of_ten = 0
    for item in rounding_list:
        rounding_num += item * (10 ** power_of_ten)
        power_of_ten += 1
    print(rounding_num * 10 ** int(decimal))

if decider_val >= 5:
    rounding_list = num_list_keep[::]
    rounding_list.reverse()
    round_value = rounding_list[0] + 1
    del(rounding_list[0])
    rounding_num = 0
    power_of_ten = 1
    for item in rounding_list:
        rounding_num += item * (10 ** power_of_ten)
        power_of_ten += 1
    print((rounding_num + round_value) * 10 ** int(decimal))
