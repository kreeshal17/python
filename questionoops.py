class Phone:
    def calling(self,press):
        if press==1:
            print("calling mom")
        elif press==2:
            print("calling dad")
        elif press==3:
            print("calling brother")
p=Phone()
p.calling(int(input("enter the number you wanna call")))

