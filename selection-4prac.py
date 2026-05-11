def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        
        # Assume the current position (i) has the minimum element
        min_index = i
        
        # Greedy Step: Find the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Print the progress after each pass
        print(f"Step {i + 1}: {arr}")
        
    return arr

# Example Usage
data = [64, 25, 12, 22, 11]
print("Original Array:", data)

sorted_array = selection_sort(data)
print("Sorted Array:", sorted_array)

































[ START ]
    |
    v
[ INPUT: Unsorted Array ]
    |
    v
+---------------------------------------+
|  OUTER LOOP (i from 0 to n-1)         | <-----------+
+---------------------------------------+               |
    |                                                 |
    v                                                 |
[ SET min_index = i ]                                 |
(Assume the first unsorted item is the smallest)      |
    |                                                 |
    v                                                 |
+---------------------------------------+               |
|  INNER LOOP (j from i+1 to n)         |               |
+---------------------------------------+               |
    |                                                 |
    v                                                 |
[ IS arr[j] < arr[min_index]? ]                       |
    |               |                                 |
  (YES)            (NO)                               |
    |               |                                 |
    v               |                                 |
[ UPDATE min_index ]|                                 |
(Found a new small) |                                 |
    |               |                                 |
    +---------------+                                 |
    |                                                 |
[ END INNER LOOP ]                                    |
    |                                                 |
    v                                                 |
[ SWAP arr[i] with arr[min_index] ]                   |
(Move the smallest found element to the sorted part)  |
    |                                                 |
    +-------------------------------------------------+
    |
    v
[ ALL ELEMENTS PROCESSED? ]
    |
    v
[ OUTPUT: Sorted Array ]
    |
    v
[ END ]
