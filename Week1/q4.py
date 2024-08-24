ipt1 = input("Enter a number: ")

def palindrome(num):
    length = len(num)

    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            return False
        return True

if palindrome(ipt1) == True:
    print("Number is palindrome")
else:
    print("Number is not palindrome")