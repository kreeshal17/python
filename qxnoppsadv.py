# define a python classs student with attributes name age and grade an a maethod is_passing  to check if the student grade is passing(>-60)
class student:
    def __init__(self,name,age ,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def is_passing(self):
        if self.grade>=60:
            print(f"{self.name} of {self.age} having grade {self.grade} has passed")
        else:
             print(f"{self.name} of {self.age} having grade {self.grade} has failed")
c= student("kree",6,89)         
c.is_passing()        
c= student("kree",6,9) 
c.is_passing()        
# define a python class Employess with attributes name position and salary and a method apply_bomus () to apply a bonus to salary Solution
          