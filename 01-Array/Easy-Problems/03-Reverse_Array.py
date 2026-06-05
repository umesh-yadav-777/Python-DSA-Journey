# method 1: using slicing
arr = [1,2,6,3,5]
reversed_arr = arr[::-1]
print(f'Reversed array using slicing: {reversed_arr}')


# method 2: using built-in function
arr = [2,4,6,8,10]
reversed_arr = list(reversed(arr))
print(f'Reversed array using built-in function: {reversed_arr}')

# method 3: using a loop
arr = [10,5,8,12,3]
reversed_arr = []
for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])
print(f'Reversed array using a loop: {reversed_arr}')


# using function
''' Here time complexity-        O(n)
    and  space complexity also-  O(n)
'''
def reverse_array(arr):
    reversed_arr = []
    for i in arr:
        reversed_arr.insert(0, i)
    return reversed_arr

arr = [10,15,20,5,7]
print(f'Reversed array using a function: {reverse_array(arr)}')



# method 5: using a class
class ReverseArray:
    def __init__(self, arr):
        self.arr = arr

    def reverse(self):
        reversed_arr = []
        for i in range(len(self.arr)-1, -1, -1):
            reversed_arr.append(self.arr[i])
        return reversed_arr
arr = [1,2,6,3,5]
reverser = ReverseArray(arr)
print(f'Reversed array using a class: {reverser.reverse()}')


# Best case
'''
 Here time complexity-        O(n)
 and  space complexity also-  O(1)
'''

def reverse_arr(arr):
    first = 0
    last = len(arr)-1

    while first < last:
        # swap
        arr[last], arr[first] = arr[first],arr[last]
        first += 1
        last -= 1
    return arr
arr = [2,4,6,8,10]
print("Reverse arr: ",reverse_arr(arr))
