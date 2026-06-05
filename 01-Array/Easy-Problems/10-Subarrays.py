
'''
Print all subarray from a array.



'''

def print_subarray(arr):
    ts = 0
    for i in range(len(arr)):
        for j in range(i , len(arr)):
            for k in range(i , j+1):
                print(arr[k],end=' ')
            ts += 1
            print()
        print()
    print("Total subarrays is :",ts)
    return arr

arr = [2,4,6,8,10]
print_subarray(arr)
