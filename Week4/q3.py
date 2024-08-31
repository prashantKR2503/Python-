num = [5, 9, 7, 3, 8]


def square(num):
    for i in range(len(num)):
        num[i] = num[i] * num[i]
    return num


print(square(num))
