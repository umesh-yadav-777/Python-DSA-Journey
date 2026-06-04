# using loop
arr  = [10, 5, 8, 12, 3]
largest = second_largest = float('-inf')

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(f'The second largest element is: {second_largest}')


# using function
def second_largest_element(arr):
    largest = second_largest = float('-inf')
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest
arr = [10,15,18,5,12]
print(f'The second largest element is: {second_largest_element(arr)}')


# using class
class SecondLargestElement:
    def __init__(self, arr):
        self.arr = arr

    def find_second_largest(self):
        largest = second_largest = float('-inf')
        for i in self.arr:
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest and i != largest:
                second_largest = i
        return second_largest

arr = [11,14,18,5,12]
second_largest_finder = SecondLargestElement(arr)
print(f'The second largest element is: {second_largest_finder.find_second_largest()}')



