# # class A:
# #     def aa(self):
# #         return "Class A"
# # class B(A):
# #     def bb(self) :
# #         return "class B"
# # class C(A,B)    :
# #     def cc(self):
# #         return "class cc"
    
    
# # class Building:
# #     def __init__(self, area, floor, room):
# #         self.area = area
# #         self.floor = floor
# #         self.room = room

# #     def into(self):
# #         print("Total area:", self.area)
# #         print("Total floors:", self.floor)
# #         print("Total rooms:", self.room)

# # class School(Building):
# #     def __init__(self, area, floor, room, teacher, student):
# #         super().__init__(area, floor, room)
# #         self.teacher = teacher
# #         self.student = student

# #     def into(self):
# #         super().into()
# #         print("Total teachers:", self.teacher)
# #         print("Total students:", self.student)

# # a = School("100 acre", 45, 234, 54, 676)
# # a.into()

# class Building:
#     def __init__(self,area,floor,room):
#         self.area=area
#         self.floor=floor
#         self.room=room
#     def into(self):
#         print("total area ",self.area)
#         print("total  floor",self.room)
#         print("total  room ",self.floor)
    
# class School(Building):
#     def __init__(self,area,floor,room,teacher,student):
#         self.area=area
#         self.floor=floor
#         self.room=room
#         self.teacher=teacher
#         self.student=student
#     def into(self):
       
#         print("total teacher ",self.teacher)
#         print("total  student ",self.student)
# a=School("100 acre",45,234,54,676)
# a.info_Building()
# class Aa:
#     def rr(self):
#         print("Aa")
# class Aa1(Aa):
#     def rr(self) :
#         super().rr()      
#         print("Aa1")
# a=Aa1()  
# a.rr()
class T  :    
 def hh(self, a=None,b=None):
    if a!=None and b!=None:
        y=a*b
        print(y)
    elif a!=None:
        print(a**2)    
    else:
        print("there is  no Argument")    
t=T()
t.hh(3,4)        