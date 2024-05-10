# createa a clss college
# add instance name it "detail" like  no of classl,ocation, no of teacher 
# add instance name it return no of classes
# add instance name it return no of teacher
# # add instance name it location of college
# class College:
#     def details(self,number_class,location,teacher_num):
#      self.number_class=number_class
#      self.location=location
#      self.teacher_num=teacher_num


#     def classes(self)  :
#        return self.number_class
#     def  teachers(self):
#        return self.teacher_num
#     def locatioon(self):
#        return self.location
# c=College()
# print(c.details(10,"butwal",89))
# print(c.classes())
# print(c.teachers())
# print(c.locatioon())

class Cylinder:
    def details(self,pie,r,h):
        self.pie=pie
        self.r=r
        self.h=h
        
    def TSA(self)    :
        return 2*self.pie*self.r*self.h
c=Cylinder()
c.details(22/7,4,5)
print(c.TSA())


    
class Cone:
    def detail(self,r,l,pie):
        self.r=r
        self.l=l
        self.pie=pie
    def TSA(self)    :
        return self.pie *self.r*(self.r+self.l)
    def CSA(self)    :
        return self.pie *self.r*self.l
c=Cone()
c.detail(int(input("enter the raduis")),int(input("enter the length")),22/7)
print(c.TSA())
print(c.CSA())
   
    