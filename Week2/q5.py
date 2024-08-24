ipt1 = int(input("Enter the number"))

length = len(str(ipt1))

def add(ipt1):
    num1 = 0
    for i in range(1, ipt1 + 1):
        num1 += ipt1 % 10
        ipt1 = ipt1 // 10
    return num1

print(add(ipt1))