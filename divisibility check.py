number = int(input("select number "))
for item in range(1,number + 1):
    divisors = (number % item)
    if divisors == 0:
        print(item)