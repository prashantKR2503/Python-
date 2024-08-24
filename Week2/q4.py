ipt1 = int(input("Enter a number: "))

def factorial(ipt1):
    num = 1
    for i in range(1, ipt1 + 1):
        num = num * i
    return num

print(factorial(ipt1))
