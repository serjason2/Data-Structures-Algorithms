# DSA QuickSort
# As the name suggests, Quicksort is one of the fastest sorting algorithms

# The Quicksort algorithm takes an array of values , chooses one of the values as the 'pivot' element, and moves the other values so that
# lower values on the left of the pivot element, and higher values are on the right of it.

# Manual Run Through
[11, 9, 12, 7, 3]
[3]
[3, 9, 12, 7, 11]
[12, 7]
[3, 9, 7, 11, 12]
[9, 7] # 7 is the pivot
[3, 7, 9, 11, 12]
# To sum up, the Quicksort algorithm makes the sub-arrays become shorter and shorter until array is sorted.

# QuickSort Implementation

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index-1)
        quickSort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quickSort(my_array)
print("Sorted array: ", my_array)


# Time Complexity:
# O(nlog n)

# Worst Case: O(n^2) | This is when the pivot element is either the higher or lowest value in every sub-array, which leads to a lot of
# recursive calls.