# DSA Arrays
# An array is a data structure used to store multiple elements.

my_array = [7, 12, 9, 4, 11]
print(my_array[0])  # Outputs 7

# Example
minVal = my_array[0]    # Step 1

for i in my_array:        # Step 2
    if i < minVal:      # Step 3
        minVal = i

print("Lowest value:", minVal)

# Algorithm Time Complexity
# In the example above, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is because the algorithm
# must visit every array element one time to find the lowest value. The loop must run 5 times since there are 5 values in the array. And if the array had
# 1000 values, the loop would have to run 1000 times.