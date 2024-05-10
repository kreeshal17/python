import numpy as np
# k=[1,2,3,4,5,6,7]
# arr=np.array(k)
# print(arr)
# print(type(arr))

#creating 2d array

# u1=[1,2,34,5,68,8]
# u2=[14,2,634,55,68,80]
# a2=np.array([u1,u2])
# print(a2)

# print(a2.shape)

u1=[1,2,3,4,5]
u2=[6,7,8,9,10]
u3=[11,12,13,14,15]
u4=[16,17,18,19,20]
a2=np.array([u1,u2,u3,u4])
print  (a2)
print  (a2.shape)
print(a2[0,2])
print(a2[2:,3:])#extract 14 15 19 120
#extract  3 4 
         #8 9
print(a2[0:2,2:4])         
print(np.mean(a2))
print(np.median(a2))
print(np.where(a2==14,400,a2))