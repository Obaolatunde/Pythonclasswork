list_of_numbers=[20,35,60,40,30]
def sum_list(number_list):
    total=0
    for items in number_list:
        total+=items
    return total*len(number_list)
print (sum_list(list_of_numbers))
