# DSA Bubble Sort
# Bubble sort is an algorithm that sorts an array from the lowest value to the highest value.

# 1. Go through the array, one value at a time.
# 2. For each value, compare the value with the next value.
# 3. If the value is higher than the next one, swap the values so that the highest value comes last.
# 4. Go through the array as many times as there are values in the array.

# Manual Run Through
# [7, 12, 9, 11, 3]
# [7, 9, 12, 11, 3]
# [7, 9, 11, 12, 3]
# [7, 9, 11, 3, 12]
# Will keep looping until 3 is the shortest and until it is fully sorted.

# Bubble Sort Implementation
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)

# Bubble Sort Improvement
my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)


# Bubble Sort Time Complexity
# O(n^2)
# After one loop, the array is looped through again and again n times.
# Quicksort is an sorting algorithm that is faster than this.