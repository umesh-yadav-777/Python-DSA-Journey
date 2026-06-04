nums = [1,2,6,3,5]
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i
print(f'The largest element is: {largest}')


# with function
def largest_element(nums):
    largest = nums[0]

    for i in nums:
        if i > largest:
            largest = i
    return largest

nums = [10,5,8,12,3]
print(f'The largest element is: {largest_element(nums)}')


# with class
class LargestElemnt:
    def __init__(self, nums):
        self.nums = nums

    def find_largest(self):
        largest = self.nums[0]
        for i in self.nums:
            if i > largest:
                largest = i
        return largest

nums = [10,5,8,12,3]
largest_finder = LargestElemnt(nums)
print(f'The largest element is: {largest_finder.find_largest()}')

