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

MyList = [54,26,93,17,77,31,44,55,20] # this will assign the values to the unsorted list
print ("This is the unsorted list" + str(MyList)) # this will print the unsorted list
mergeSort(MyList) # this will run the unsorted list through the Merge Sort algorithm funciton
print("\nThis is the sorted list using Merge Sort: " + str(MyList)) # this will print the sorted list