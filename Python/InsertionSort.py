# DSA Insertion Sort
# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values
# that are not sorted yet.

# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array,
# until the array is sorted.

# Manual Run Through
[7, 12, 9, 11, 3] # Unsorted
[7]
[12]
[9]
[7, 9, 12, 11, 3]
[12]
[11]
[7, 9 ,11, 12, 3]
[3]
[3, 7, 9, 11, 12] # Sorted

# Insertion Sort Implementation
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print("Sorted array 1: ", my_array)


# Improved Solution
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array 2: ", my_array)


# Time Complexity:
# O(n^2)
