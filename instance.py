# # class Phone:
# #     def calling (self):
# #         print(self.data)
        
# # Phone.data="ram"       
# # Phone().calling()   
# class Phone:
#     def calling(self,name):
#         print("calling to",name)
#     def camera(a):
#         print("open camera",a.data) 
#     def close(a):
#         print("clsoe the last opem app")      
# d=Phone()        
# d.calling("kreeshal")
# Phone.data="ram"
# d.camera()
class Car:
    def work(self,press):
        if press==1:
            print("car is starting")
        elif press==2:
            print("car is not moving")   
        elif press==0:
            print("car has stopped")
c=Car()
c.work(int(input("ask the number")))

