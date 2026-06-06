'''
Find the maximum sum of a subaarray

'''

# Brut Froce Approch ,  TC = O(n*n*n)
def max_subarray_sum(arr):
    max_sum = float("-inf")

    for i in range(len(arr)):
        for j in range(i , len(arr)):
            curr_sum = 0

            for k in range(i , j+1):
                curr_sum += arr[k]
            print(curr_sum)
            if max_sum < curr_sum:
                max_sum = curr_sum
    print()
    return max_sum

arr = [1,-2,6,-1,3]
print("Brut Force - Maximum sum = ",max_subarray_sum(arr))
print()





# Better approch using- (Prefix sum)

def max_subarray_sum(arr):
    n = len(arr)

    # create prefix sum of array
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1,n):
        prefix[i] = prefix[i-1] + arr[i]

    max_sum = float ("-inf")

    # Generate all subarray
    for i in range(n):
        for j in range(i,n):

            if i == 0:
                curr_sum = prefix[j]
            else:
                curr_sum = prefix[j] - prefix[i-1]

            max_sum = max(max_sum, curr_sum)
    return max_sum

arr = [1,-2,6,-1,3]
print("Using Prefix Sum - Maximum sum=",max_subarray_sum(arr))
print()





'''
Best Approach Kedane's Algorithms
TC = O(n), SC = O(1)
'''
   # This code only work when mixed number negative and positive if user inpte all negative number then this code max_sum return 0 always.
def max_subarray_sum(arr):
    curr_sum = 0
    max_sum = float('-inf')

    for num in arr:
        curr_sum += num

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    return (max_sum)

arr = [-2,-3,4,-1,-2,1,5,-3]

print("Kedane's Algorithm - Maximum sum = ", max_subarray_sum(arr))


# So, This code worked on all types of input mixed numbers, all negative numbers

# Interviewer Expacted this code.
def max_subarray_sum(arr):
    curr_sum = 0
    max_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])

        max_sum = max(max_sum, curr_sum)

    return max_sum

arr = [-3, -5, -2, -8]
print("Kedane's Algorithm - Maximum sum = ", max_subarray_sum(arr))



