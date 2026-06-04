arr = [1, 2, 3, 2, 4, 5, 1]
unique_arr = []

for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)

print(f'The array after removing duplicates is: {unique_arr}')


# using function and sorted it
def remove_duplicates(arr):
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    return unique_arr

arr = [5,2,3,2,4,6,5,1,8,2,1]
print(f'The array after removing duplicates is: {remove_duplicates(arr)}')


# using function and sorted it
def remove_duplicates(arr):
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    return sorted(unique_arr)

arr = [5,2,3,2,4,6,5,1,8,2,1]
print(f'The array after removing duplicates is: {remove_duplicates(arr)}')



# using class
class RemoveDuplicates:
    def __init__(self, arr):
        self.arr = arr

    def remove_duplicates(self):
        unique_arr = []

        for i in self.arr:
            if i not in unique_arr:
                unique_arr.append(i)
        return sorted(unique_arr)
arr = [5,2,3,2,4,6,5,1,8,2,1]
remover = RemoveDuplicates(arr)
print(f'The array after removing duplicates is: {remover.remove_duplicates()}')
