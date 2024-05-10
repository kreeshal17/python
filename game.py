import random
a=int(input("enter the number"))
b=random.randint(3, 50)
while a!=b:
    if a>b:
        print("the number is bigger ")
    elif a<b:
        print("the numbr is as small as your's ***")
    else:
        print("you won huehue")
        continue   
        