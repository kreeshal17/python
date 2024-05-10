# 'first we will create a class
#     class is the blueprint of an object first letter of class should be capital
# class Car:
#  name="Audi"
# wheels=4
#  engine="2500 cc"
#     type="petrol"
# c=Car
# c.wheels=6 #changing or updating a data
# print(c.wheels)
# c.name="mercedes"
# print(c.name)
# print(Car.name)
# #create a class for phone
class Phone:
    name="vivo x 60 pro"
    storage="256 gb"
    ram="12 gb"
    model="2021"
    battery="4500 mah"
c=Phone
c.name
c.battery
c.storage  
class Phone:
    def calling(self):
      print("calling")
p=Phone()
print(p.calling())
class Phone:
    def calling(self,name):
        print("calling to",name)
    def camera(self):
        print("open camera")
    def close(self):
        print("close the last opened app")
d=Phone()
d.calling("brihat")
d.camera()
class Phone:
    def calling(self,press):
        if press==1:
            print("calling mom")
        elif press==2:
            print("calling dad")
        else:
            print("calling brother")
    def function(self,press):
        if press==1:
            print("open camera")
        elif press==2:
            print("click photo")
        else:
            print("close camera")
c=Phone()

c.calling(1)
c.function(1)
class Student:
    def avg_score(self,maths,english,hindi,science):
        self.maths=maths
        self.english=english
        self.hindi=hindi
        self.science=science
        return(self.maths+self.english+self.science+self.hindi)/4
# s=Student()
# print("the average score is ", s.avg_score(44,45,47,48))'''
# create a class marksheet
# create a instance only to asign subjects and mention subjects add another instance nameed it total_score

class Marksheet:
    def assign(self,m,p,c,b,h):
        self.maths=m
        self.physics=p
        self.chemistry=c
        self.biology=b
        self.hindi=h
       

    def total_score(self):
        return self.maths+self.physics+self.chemistry+self.biology+self.hindi
    
    def min_score(self):
        return(min(self.maths,self.physics,self.chemistry,self.biology,self.hindi))
    def max_score(self):
        return(max(self.maths,self.physics,self.chemistry,self.biology,self.hindi))
    
s=Marksheet()
s.assign(42,44,45,46,47)
print(s.total_score())
print(s.min_score())
print(s.max_score())


