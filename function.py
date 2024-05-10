# def sum(x,y):
#     print(x+y)
#     # ki ta bhitra print garnu parxa ki ta return garnu parxa ani bahira call gaerera function call garnu parxa
  
# def sum(x,y):
#     return x+y
# print(sum(8,4))

# def cube(x):
#     return x**3
# def cuberoot(x):
#     return x**(1/3)
# def squareroot(x):
#     return x**(1/2)
# def square(x):
#     return x**2
# print(f"the square is {square(5)}")
# print(f"the squareroot is {squareroot(25)}")
# print(f"the cuberoot is {cuberoot(27)}")
# print(f"the cube is {cube(3)}")
  
# def circle():
#     r=float(input("enter the radius"))
#     pie=22/97
#     return pie*r**2
# print(circle())    
# def triangle():
#     h=int(input("enter the height"))
#     b=int(input("enter the breadth"))
#     return b*h/2
# print(triangle())

# def checknum():
#     x=int(input("enter the number you wanna check"))
#     if x>0:
#         return "positive"
#     elif x==0:
#         return "zero"
#     else:
#         return "negative"
# print(checknum())    
    
#check first letter of string is vowel or not
# def checkvowb():
#     i=input("enter the string")
#     c=i.lower()
#     if c[0] in ["a","e","i","o","u"]:
#         return "vowel"
#     else:
#         return "consonent"
# print(checkvowb()) 

    
# def checkvow():
#     i = input("Enter the string: ")
#     k = len(i) - 1Kree
#     c = i.lower()
#     if c[k] in ["a", "e", "i", "o", "u"]:#if x[-1] in "aeiou"
#         return "vowel"
#     else:
#         return "consonant"

# print(checkvow())
# def capital():
#      i=input("enter the string")
#      if i[0]==i[0].upper():#if i=i.capitalize()
#           return "yes"
#      else:
#           return "false"
# print(capital())     
     

def calculate ():
    x= input ("want you want to calcualte")
    if x.lower()=="square":
     v =float(input("enter the value for square"))
     return v**2
    elif x.lower()=="cube ":
        v=float(input("enter value for cube"))
        return v**3
    elif x.lower()=="squareroot":
        v=float(input("enter value for squareroot"))
        return v**(1/2)
    elif x.lower()=="cuberoot":
        v=float(input("enter value for cuberoot"))
        return v**(1/3)
    
print(calculate())