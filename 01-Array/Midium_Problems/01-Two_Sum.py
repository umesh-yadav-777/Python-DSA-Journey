'''
Find the two sum of am array.
example:
        arr[2,7,11,13,15]
        sum = 9

      print[2,7] or [0,1]

'''

# It return only one pair
  # Brut Force Approch , Time Comlexit = O(n*n)
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return(i , j)
    print()
    return []

arr = [2,11,7,13,15]
target = 9

print(two_sum(arr,target))

# It returns all pairs , TC= O(n*n)

def two_sum(arr, target):
    pairs = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))

    return pairs

arr = [2,7,11,13,15,1,8]
target = 9

print(two_sum(arr, target))

# Optimize Solution, TC= O(n), SC = O(n)
            #  best case
def two_sum(nums, target):
    seen ={}

    for i in range(len(arr)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
