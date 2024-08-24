inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))

def q1( inp1, inp2 ):
    mul = inp1 * inp2
    if mul <= 5000:
        sum1 = inp1 + inp2
        return sum1
    return mul

num = q1(inp1, inp2)
print(num)