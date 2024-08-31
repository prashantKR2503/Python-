
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
def cal_sum_sub(num1, num2):
    add = num1 + num2
    sub = num1 - num2

    return add, sub

print(cal_sum_sub(num1,num2))