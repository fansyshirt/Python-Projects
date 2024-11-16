first = float(input("choose first number "))
operator = float(input("choose operator (1= +) (2= -) (3= x) (4= /)"))
second = float(input("choose second number "))
if operator == 1:
    sum = first + second
if operator == 2:
    sum = first - second
if operator == 3:
    sum = first / second
if operator == 4:
    sum = first * second
print("= " + str(sum))
