# # # # # # # a=[1,2,3,4,5,55,5,5,55,55,5,5,]
# # # # # # # # # print(type(a))
# # # # # # # # # c=a.append(55)
# # # # # # # # # print(a)
# # # # # # # # # d=a.pop()
# # # # # # # # # print(d)
# # # # # # # # f=a.remove(1)
# # # # # # # # print(a)
# # # # # # # # a.insert(5,10)
# # # # # # # # #it will insert the element in a  given index
# # # # # # # # print(a)
# # # # # # # # a.extend([2,3,4,5,6])
# # # # # # # # print(a)
# # # # # # # # d=a.count(55)
# # # # # # # # print(d)
# # # # # # # a.sort()
# # # # # # # print(a)
# # # # # # # a.sort(reverse=True)
# # # # # # # print(a)
# # # # # # # a.clear()
# # # # # # # print(a)
# # # # # # # s=[1,2,3,4,56,78,96,13,'hello',,'robin',[1,2,3,4,]]
# # # # # # #some qxn to perform the experiment from the example
# # # # # # # 1. find the largest number
# # # # # # 2.find the smallest number
# # # # # # 3. waht is the total of the list
# # # # # # 3. waht is the avearage of the list
# # # # # # 4.add789, 456, 789  using single function
# # # # # # 5. remove 3 from the list
# # # # # # 6. add karan on the 6th index
# # # # # t=[44,88,66,3,4,7,9,5,2,13,5,100,1023]
# # # # # t.sort()
# # # # # print("the smallest number is",t[0])
# # # # # t.sort(reverse=True)

# # # # # print("the largest number is",t[0])
# # # # # sum1=sum(t)
# # # # # print("the sum i s",sum1)
# # # # # av=sum1/len(t)
# # # # # print(av)
# # # # # t.extend([789,456,789])
# # # # # print(t)
# # # # # t.remove(3)
# # # # # print(t)
# # # # # t.insert(6,"karan")
# # # # # print(t)
# # # # r="hello this is the 4th class"
# # # # print(type(r.split()))
# # # u = [1, 2, 3, [7, 8, ['hello', 'this', 'is', 'the', '4th'], 9], 1, 2, 3]
# # # u[-4][-2][2] = u[-4][-2][2].replace("i", "a")

# # # print(u)
# # t=[]
# # print(type(t))
# # t=[1,2,3,4,5,6,7,8,99]
# # f=t.append(44)
# # print(f)
# # # tuple 
# # w=(1,2,3,4,5)
# # print(type(w)


q={1,2,3,4,5,6,7,8,9}
r={11,12,4,5,34,54,55,43,33}
print(q.symmetric_difference(r)) #it wont show common element
# print(q.union(r))
# print(q.intersection(r))
# a=34
# b=23
# print(f"the name is {a} and b is {b}",a+b)
