'''
Approach 1: Brute Force
           Time compexity = O(n*n)

'''

def trap(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water

height = [4,2,0,6,3,2,5]
print(trap(height))



'''
Approach 2: Prefix & Suffix Arrays
Time comlexity = O(n)
'''

def trap(height):
    n = len(height)

    left_max = [0] * n
    right_max = [0] *n

    left_max[0] = height[0]

    for i in range(1,n):
        left_max[i] = max(left_max[i-1], height[i])
        right_max[n-1] = height[n-1]

    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
        water = 0

    for i in range(n):
        water+= min(left_max[i], right_max[i]) - height[i]

    return water

height = [4,2,0,3,2,5]
print(trap(height))


'''
Approach 3: Optimal Two Pointer
Time COmlexity : O(n)
'''

def trap(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water

height = [4,2,0,6,3,2,5]
print(trap(height))



