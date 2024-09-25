import random

string = input("Enter a String : ")
c = random.choices(string,k=1)

print(f"random character from the string : {c}")
