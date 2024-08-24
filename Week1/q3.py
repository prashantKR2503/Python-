lst = []

for i in range(1,21):
    inp1 = int(input("Enter a number: "))
    lst.append(inp1)

for num in lst:
    if num % 5 == 0:
        print(num)