def greet():
    name=input("enter the name ")
    roll=int(input("enter the age "))
    print(f"good morning {name}  {roll}")

greet()   

def palindrone():
    str= input("enter the name tp check")
    str2=str[::-1] 
    if(str==str2):
        print("the name is palindrone ")
    else:
        print("it is not palindrome")    
palindrone()        