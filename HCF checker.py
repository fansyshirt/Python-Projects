a = int(input("value a   "))
b = int(input("value b   "))
while a != b:
    if a > b:
        a -= b
    if b > a:
        b -= a
    print(a, ", ", b)