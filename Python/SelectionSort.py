# DSA Selection Sort
# The selection sort algorithm finds the lowest value in an array and moves it to the front of the array.

# The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

# Manual Run Through:
[7, 12, 9, 11, 3] # 3 is the lowest
[3, 7, 12, 9, 11] # move to the front and shift all the elements right
[3, 7, 9, 12, 11] # move 9 since it is the lowest and shift elements to the right
[3, 7, 9, 11, 12] # move 11 since it is the lowest and shift elements to the right and it is now all sorted.


# Selection Sort Implementation
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_index = my_array.pop(min_index)
    my_array.insert(i, min_index)

print("Sorted array 1st: ", my_array)


# Improved Selection Sort, using swapping:
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array 2nd: ", my_array)

# Selection Sort Time Complexity:
# O(n/2 * n) = O(n^2)