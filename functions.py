##Functions allows for re-usability. functions are meant to do one thing and do them well
##def==define. functions wont run except called
##argument==
##cassave==argument, machine==function, mill==return(terminates fn execution)
##docstring==documentation
##e.g def testfunc():
##	 "This is not a yeye function. na test"
##	 return "Bye, Learner"
##the print function returns the return statement. print (testfun()) will show Bye, Learner
def even_numbers(startpoint, endpoint):
    even_numbers=[]                    
    for  number in range(startpoint, endpoint):
        if number%2==0:
            even_numbers.append(number)
    return even_numbers #return statement is the last thing a funtion does
print(even_numbers(0,200))
                                        
def even_numbers(startpoint, endpoint=100): #default argument
    even_numbers=[]                    
    for  number in range(startpoint, endpoint):
        if number%2==0:
            even_numbers.append(number)
    return even_numbers #return statement is the last thing a funtion does
print(even_numbers(5))

def generatenumber():
    start=input("Biko, enter number make i start\t")
    while not start.isdigit():
        print("Nna mehn, put number dia")
        start=input("Biko, enter number make i start\t")
    endpoint=input("Nna, where make i stop\t")
    while not endpoint.isdigit():
        print("Nna mehn, put number dia")
        endpoint=input("Nna, where make i stop\t")
    print(even_numbers(int(start),int(end)))
