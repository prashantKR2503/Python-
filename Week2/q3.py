ipt1 = int(input("Enter start number: "))
ipt2 = int(input("Enter end number: "))

lst = []
def isPrime(ipt1, ipt2):
    if ipt1 < 2:
        print("enter number greater than 1")



    for i in range(ipt1,ipt2+1):
        flag = 1
        for j in range(2,i):
            if i % j == 0:
                flag = 0
        if flag == 1:
            lst.append(i)

    return lst

print(isPrime(ipt1,ipt2))