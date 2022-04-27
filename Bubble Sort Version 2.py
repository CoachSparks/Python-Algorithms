# This Python program will use the Bubble sort algorthim to sort a list of data
# Ronnie Sparks
# This is written for Python 3 on 4/26/2022

def bubble(list_a):
    indexing_length = len(list_a)-1  #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.

# These are the array values, you can change these to any and as many values as you want.
print(bubble([4,8,1,14,8,2,9,5,7,6,6])) 

