def errorhandelling():
    try:
        a=5
        print(a)
    except Exception as e:
        print(e)    
    else:
        try:   
            f=3
            k=0
            print(f/k) 
        except  ZeroDivisionError:
            print("error ho zero le div na") 
       
    finally:
        try:
            a=3
            b="kreeshal"
            print(a/b) 
        except  TypeError:
             print("farak type") 
errorhandelling()
print("kreeshal ")                     
             