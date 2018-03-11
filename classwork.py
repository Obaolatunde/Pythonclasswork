def classwork():
    classwork=[]
    start=input("Biko, enter number make i start\t")
    while not start.isdigit():
        print("Nna mehn, put number dia")
        start=input("Biko, enter number make i start\t")
    end=input("Nna, where make i stop\t")
    while not end.isdigit():
        print("Nna mehn, put number dia")
        end=input("Nna, where make i stop\t")
    for  number in range(int(start),int(end)):
        if number%3==0:
            classwork.append(number)
    print("The classwork of the numbers in range",start,"to",end, "is",len(classwork)*sum(classwork))
    print("\nThis contains",len(classwork),"numbers that adds up to",sum(classwork))
    
