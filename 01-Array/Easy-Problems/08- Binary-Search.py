def binary_search(arr, key):
    start = 0
    end = len(arr)-1


    while (start <= end):
        mid = (start + end) // 2

        # comparisons
        if arr[mid] == key:  # Found
            return mid

        if arr[mid] < key:     # Update right half
            start = mid + 1

        else:                  # Update Left half
            end = mid - 1

    return -1

arr = [2,4,6,8,10,12,14]
key = 4
print("Index for key is : ",binary_search(arr,key))
