class Vehicle():
    def __init__(self,kind,year_of_manufacture,cost,speed,no_of_wheels):
        self.speed=speed
        self.kind=kind
        self.year_of_manufacture=year_of_manufacture
        self.cost=cost
        self.no_of_wheels=no_of_wheels
    def can_fly(self):
        return self.kind=="Aeroplane, c'mon"
    def sound_hound(self):
        return "pipipii"
    def can_sail(self):
        return self.kind=="Ship Mehn"
    def accellerate(self,value):
        self.speed+=value
        return self.speed


    
class Car(Vehicle):
    pass
