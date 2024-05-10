import random as rm
# print(rm.random())
# print(rm.randint(2,8))
# for i in range(6):
#     print(rm.randrange(0,9))
#f=[1,2,3,4,5,6,7,8,9,0]
# f="0123456789"
# print("".join(rm.sample(f,k=6)))
# # d=[]
# # for i in range(0,11):
# #     y=rm.randrange(0,20)
# #     d.append(y)
# print(d)    

#append only 20 even element in the list
# for i in range(500):
k=[]
while len(k)!=20:
    y=rm.randint(500)
    if(y%2==0):
         k.append(y)

print(k)        

import matplotlib.pyplot