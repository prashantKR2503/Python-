text = input("Enter the string: ")

length = len(text)
num = 0
if length%2 == 0:
    num1 = (length-1)//2
    for i in range(0, num1-2):
        print(text[num])
        num += 2
else:
    num1 = (length + 1) // 2
    for i in range(0, num1):
        print(text[num], end='')
        num += 2