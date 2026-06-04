nums = [1,2,6,3,5]
smallest = nums[0]

for i in nums:
    if i < smallest:
        smallest = i

print(f'The smallest element is: {smallest}')

# with function

def smallest_element(nums):
    smallest = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest

nums = [10,5,8,12,3]
print(f'The smallest element is: {smallest_element(nums)}')


# with class
class SmallestElement:
    def __init__(self, nums):
        self.nums = nums

    def find_smallest(self):
        smallest = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] < smallest:
                smallest = self.nums[i]
        return smallest

nums = [11,15,8,5,7]
smallest_finder = SmallestElement(nums)
print(f'The smallest element is: {smallest_finder.find_smallest()}')

