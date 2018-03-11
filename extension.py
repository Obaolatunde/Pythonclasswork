from Module_dir.Shapescalc import Shapes_calculator as SC

class Mathcalc(SC):
    def perimeter_rectangle(self,lenght,breadth):
        return (lenght+breadth)*2

    def perimeter_circle(self):
        radius=input("\tInput Radius\t")
        message = "The perimeter of the circle with radius " + str(radius) + " is " + str(self.pi*float(radius)*2)
        return message
    
    

#oop Steps
    # 1. Create class using the class keyword
    # 2. instantiate the class i.e create an object from the class
    # 3. Perform action on the object created
    
#isintance
new_object=Mathcalc()
if isinstance(new_object,Mathcalc):
    print("Truest")
