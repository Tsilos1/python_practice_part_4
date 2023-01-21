#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(x, y, z):
    return max([x, y, z])

print (max_num(1, 2, 3))

# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(list):
    #if empty list, return 0
    if len(list) == 0:
        return 0
    #product starts with first element of list
    prod = list[0]
    
    #Go through list elements and multiply them together
    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i
            
    return prod

print(mult_list([2, 4, 6]))