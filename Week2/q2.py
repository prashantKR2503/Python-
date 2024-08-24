ipt1 = int(input("Enter a number: "))

length =0

while ipt1 > 0:
    ipt1 = ipt1 // 10
    length = length + 1
print(length)