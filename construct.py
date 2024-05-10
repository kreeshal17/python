class Car:
    def __init__(self,hp,name,door,Type):
        self.hp=hp
        self.name=name
        self.door=door
        self.Type=Type
    def details(self)    :
        print(self.hp)
        print(self.name)
        print(self.door)
        print(self.Type)
c=Car(233,"bmw",4,"petorl")     
c.details()     