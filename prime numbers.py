divisors = 0

for number in range(1, 9999999999):
    divisors = 0
    for item in range(1, number + 1):
        divisor = (number % item)
        if divisor == 0:
            divisors += 1
        if item == number and divisors == 2:
            print(number)
