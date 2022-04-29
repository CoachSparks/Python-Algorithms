# This Python program will use the Quick sort algorthim to sort a list of data
# Ronnie Sparks
# This is written for Python 3 on 4/26/2022

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() # this will remove the last element and return it as the pivot value
        
    items_greater = [] # this will be a list of values greater than the pivot value
    items_lower = [] # this will bea a list of values less than the pivot value
    
    for item in sequence:
        if item > pivot: # this will check if the current item is greater than the pivot
            items_greater.append(item) # this will append or add the item to the items_greater list
            
        else:
            items_lower.append(item) # this will append or add the item if it is less or equal to the pivot
            
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([6,3,0,1,7,5,9,2,8])) # this will print the sorted list using quick sort
            
