# This Python program will use the merge sort algorthim to sort a list of data entered by the user
# Ronnie Sparks
# This is written for Python 3 on 4/26/2022

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
                myList[k] = left[i]
              # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


MyList = [] # this will create an empty list

# create a while loop to accept user input to populate MyList
while True: # setting this to True will run the loop until it is set to False
    data = int(input("Enter and integer to add to the list: ")) # this will prompt the user to enter an integer for the list
    MyList.append(data) # this will take the entered number and add it to the MyList variable
    
    choice = (input("Would you like to enter another number?? (y / n) : ")) # this will ask if the user wants to enter another value
    if choice.lower() == 'n': # this will convert the entered character to lowercase and if it is n for no the loop will stop
        break
    
    
print ("\nThis is the unsorted list" + str(MyList)) # this will print the unsorted list
mergeSort(MyList) # this will run the unsorted list through the Merge Sort algorithm funciton
print("\nThis is the sorted list using Merge Sort: " + str(MyList)) # this will print the sorted list

