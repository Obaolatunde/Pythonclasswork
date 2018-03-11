##drink={"readymade":"carbonated","homemade":["coffee","water",("herbaltea","celerontea","blacktea")]}
##print(drink)
##DICTIONARY USE
##         key:    Value#a dictionary does not consider position. it goes randomly
##itemdict={"Name":"Omar Bongo","Colour":"Black","Job":"Thievery"}
##for gbam in itemdict:
##    print(gbam)#This prints only the dictionary keys.
##    print(itemdict[gbam],end="")#this is to print the 
##for gbam in itemdict:
##    if not type(itemdict[gbam])==dict:
##        print(itemdict[gbam])
##    elif:
##        for gag in itemdict[gbam]:
##            print(gag)
"""itemdict={"key":"person","preference":["beans","moin moin","pizza",("fun","games","football")]}
for item in itemdict:
    if type(itemdict[item])==list or type(itemdict[item])==tuple:
        for inneritem in itemdict[item]:
            print(inneritem)
    elif type(itemdict[item])==dict:
        for dictitem in (itemdict[item]):
            print(itemdict[item][dictitem])
    else:
        print(itemdict[item])"""
def extract_items(itemsequence):
    if type(itemsequence)==dict:
        for item in itemsequence:
            if type(itemsequence[item])==dict:
                print(itemsequence[item])
            elif type(itemsequence[item])==list or type(itemsequence[item])==tuple:
                for inneritem in(itemsequence[item]):
                    extract_items(inneritem)#Recursion
            else:
                print(itemsequence[item])
    elif type(itemsequence)==list or type(itemsequence)==tuple:
        for item in itemsequence:
            extract_items(item)
    else:
        print(itemsequence)
item_list=["person","school",{"number":"10","passion":{"football","rugby"},"position":"19th"},("mango","fruit","church"),["school","mosque"]]
