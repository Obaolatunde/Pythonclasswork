class Shapes_calculator():
    pi=3.142
    def __init__(self):
        pass #we dont define the parameters cos d methods dont share commonalities
            
    def triangle(self,base,height):
        return base*height*0.5

    def circle(self,radius):
        return self.pi*radius**2 #self. since pi is defined outside this method

    def rectangle(self,lenght,breath):
        return lenght*breadth

    def square(self,lenght):
        return lentght**2

    def pipe(self,radius,lenght):
        return self.pi*radius**2*lenght
    
    
    
