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

MyList = [] # this will create an empty list

# create a while loop to accept user input to populate MyList
while True: # setting this to True will run the loop until it is set to False
    data = int(input("Enter and integer to add to the list: ")) # this will prompt the user to enter an integer for the list
    MyList.append(data) # this will take the entered number and add it to the MyList variable
    
    choice = (input("Would you like to enter another number?? (y / n) : ")) # this will ask if the user wants to enter another value
    if choice.lower() == 'n': # this will convert the entered character to lowercase and if it is n for no the loop will stop
        break

print ("\nThis is the unsorted list" + str(MyList)) # this will print the unsorted list
# this will run the user defined unsorted list and sort them using Insertion Sort and print the sorted list
insertion_sort(MyList)
print("\nThis is the sorted list using insertion sort" + str(MyList))