fruits = ["mango","orange","pineapple","apples","banana","grape"]
print (fruits[2])
print (fruits[2:])#print items from position 2 onwards. list starts from 0
print (fruits[:2])#prints items before position 2
print (fruits[:])#reprints the entire list
print (fruits[-3])#Negative indexing:counts the list from the back, starting at -1
fruits[4]="ice cream" #mutation of values:changing the value of a list
print (fruits[4])#all this elements can be done in a tuple excepts mutability
print (fruits[2:3])
print(fruits)
print (len(fruits))#to count the number of items in the list
for items in fruits:#defines a one-time variable visible within the block of code
    print (items)#prints items (defined in the prior line) one after the other

#list in a list
items=["clothes",["bags","shoes","pen"],"dog","house"]
print (items[1][1])#goes to position 1, then looks for what is in position 1 in the earlier position entered

#using range

#range(start,end,step) #starts at starting number. ends at end number-1
for num in range(100):
    print(num)

for num in range(100):#considers all numbers from 0 to 100
    excludes=[0,1]# create a list of numbers you dont want to consider
    if num%2==0 and num not in excludes: #use of modulus
        print (num)

#use of random #lottery

import random
soups=["banga","ogbono","edika-ikong","bitter leaf","white soup"]
choice=random.choice(soups)
user_guess = input ("Please guess the soup Obasanjo stole\t")
while user_guess!=choice:  #use while to allow the game continue
    print("Hard luck. wash your head")
    user_guess = input ("Please guess the soup Obasanjo stole\t")
else:
    print ("Yipeeeeee!!! SUCCESS!!!")
    user_guess = input ("Please guess the soup Obasanjo stole\t")

#ask user what he will like to calculate
#ask for start and end points
#display elements in range
