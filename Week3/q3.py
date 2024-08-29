text = input("Enter the string: ")

length = len(text)
num = 0
for i in range(0, length, 2):
    print(text[i], end="")
