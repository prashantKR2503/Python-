# while( true ):
#     temp = input("Enter numbers")


num = [5, 8, 9, 6, 8]

def compairLastNums(num):
    if num[0] == num[-1]:
        return True
    return False

print(compairLastNums(num))