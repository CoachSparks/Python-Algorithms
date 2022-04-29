# This program will use the Insertion Sort algorithm. Insertion sort will compare values
# to the left of the element being compared and if the current element is smaller than
# the element to the left of it they will swap positions
# Ronnie Sparks
# Programmed in Python 3 4/29/2022


def insertion_sort(list_a): # this will take a sequence of values
    # range being 1 will start at the second element to begin comparsions since
    # there is nothing to the left of the first element to compare it to.
    indexing_length = range(1, len(list_a)) 
    for i in indexing_length: # this will loop through each value in the list
        value_to_sort = list_a[i] # this will set the current item to the variable value_to_sort

        while list_a[i-1] > value_to_sort and i>0: # the while loop will sort the array until finished
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a # this will return the sorted list


# this will assign a list of unsorted values and sort them using Insertion Sort and print the sorted list
print(insertion_sort([7,8,9,8,0,7,6,5,6,-7,8,9,8,7,6,5,6,7,8]))