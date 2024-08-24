num1 = 5

for i in range(5):
    num = num1
    for j in range(num1):
        print(num, end =" ")
        num -= 1
    num1 -= 1
    print("")