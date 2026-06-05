'''
Find all possible pairs in an array
example:
    arr = [2,4,6,8,10]

    (2,4) (2,6) (2,8) (2,10)
    (4,6) (4,8) (4,10)
    (6,8) (6,10)
    (8,10)
like xthis

Time compexity =  \(O(n^2)\)
Space Complexituy = O(1)
'''

def print_pairs(arr):
    tp = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(f"({arr[i]} {arr[j]})", end=' ')
            tp += 1
        print()
    print("Total Pairs:", tp)
    return arr

arr = [2,4,6,8,10]
print_pairs(arr)
