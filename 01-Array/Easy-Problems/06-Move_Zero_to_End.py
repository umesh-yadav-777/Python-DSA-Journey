arr = [0,1,0,3,12]

# using loop

for i in range(len(arr)):
    if arr[i] ==0:
        arr.append(arr.pop(i))
print(f'The array after moving zeros to the end is: {arr}')

# using function best case
def move_zero_to_end(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(arr.pop(i))
    return arr

arr = [0,1,0,3,12]
print(f'The array after moving zeros to the end is: {move_zero_to_end(arr)}')


# using function optimized
def move_zero_to_end_optimized(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr

arr = [0,1,0,3,12]
print(f'The array after moving zeros to the end is: {move_zero_to_end_optimized(arr)}')

# using class
class MoveZeroToEnd:
    def __init__(self, arr):
        self.arr = arr

    def move_zero_to_end(self):
        non_zero_index = 0

        for i in range(len(self.arr)):
            if self.arr[i] != 0:
                self.arr[non_zero_index] = self.arr[i]
                non_zero_index += 1

        for i in range(non_zero_index, len(self.arr)):
            self.arr[i] = 0

        return self.arr
arr = [0,1,0,3,12]
mover = MoveZeroToEnd(arr)
print(f'The array after moving zeros to the end is: {mover.move_zero_to_end()}')
