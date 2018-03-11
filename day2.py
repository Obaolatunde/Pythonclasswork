##p = input("Please enter amount")
##r = input("Please enter interest rate")
##t = input("How long is the facility for")
##if p.isdigit() and r.isdigit() and t.isdigit():
##    simpleinterest = (float(p)*float(r)*float(t))/100
##    print ("The simple interest of",p,"at",r,"percent for",t,"year(s) is",simpleinterest)    
##else:
##    print ("Are you a learner? Maka eneter only numbers jor")
##    p = input("Please enter amount")
##    r = input("Please enter interest rate")
##    t = input("How long is the facility for")
##    simpleinterest = (float(p)*float(r)*float(t))/100
##    print ("The simple interest of",p,"at",r,"percent for",t,"year(s) is",simpleinterest)

shapes = ["triangle","circle","rectangle"]
print ("Bienvenue a la calculatrice du Arithmetic")
question = input ("Will you like to play with a shape?")
positive_resp=["Yes","Y","yes"]
negative_resp=["No","N","no"]
while question()is negative_resp:
    print ("Have a nice day. Please go home")
while question()is positive_resp:
    print ("\Please select a shape from the list",shapes)
selected_shape = input("Please select a shape from the list\n")

while selected_shape.lower() not in shapes:
    print ("Boda Wale, only select from the list",shapes)
    selected_shape = input("please select a shape from the list\n")
if selected_shape.lower() == "circle":
    radius = input("Please enter a number for the radius of the circle\t")
    while not radius.isdigit():
        print ("Oga Ade, enter only number jor\n")
        radius = input("Please enter a number for the radius of the circle\t")
    print ("\nThe area of the Circle with radius",radius,"is",(float(radius)**2)*22/7)
    
elif selected_shape.lower() == "triangle":
    base = input("Please enter a number for the base of the triangle\t")
    while not base.isdigit():
        print ("Oga Ade, enter only number jor\n")
        base = input("Please enter a number for the base of the triangle\t")
    height = input("Please enter a number for the height of the triangle\t")
    while not height.isdigit():
        print ("Oga Ade, enter only number jor\n")
        height = input("Please enter a number for the height of the triangle\t")
    print ("\nThe area of the Triangle with base",base,"and Height",height,"is",(float(base)*float(height))/2)

elif selected_shape.lower() == "rectangle":
    lenght = input("Please enter a number for the lenght of the rectangle\t")
    while not lenght.isdigit():
        print ("Oga Ade, enter only number jor\n")
        lenght = input("Please enter a number for the base of the triangle\t")
    height = input("Please how tall is this rectangle\t")
    while not height.isdigit():
        print ("Oga Ade, enter only number jor\n")
        height = input("Please how tall is this rectangle\t")
    print ("\nThe area of the Rectangle with lenght",lenght,"and Height",height,"is",(float(lenght)*float(height)))
