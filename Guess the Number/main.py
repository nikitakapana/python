import random

num = random.randint(1, 10)
answ = None

while answ != num:
    answ = input("pick a number betwenn 1 and 10:")
    answ = int(answ)
    if answ == num:
        print("GG! you won!")
        break
    else:
        print("never gonna give you up...")
        