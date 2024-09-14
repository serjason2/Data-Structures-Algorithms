# Data Structures & Algorithms in Python Programming Language
# ------------------------------------------------------------------------------------------------------------------------------------------
# Fibonacci Example using (For/While Loop):

# For TwoLoop:
# prev2 = 0
# prev1 = 1

# print(prev2)
# print(prev1)

# for fibo in range(10):
#     newFibo = prev1 + prev2
#     prev2 = prev1
#     prev1 = newFibo
#     print(newFibo)


# Recursion (A function that calls itself):
# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev2 = prev1
#         prev1 = newFibo
#         count += 1
#         fibonacci(prev1, prev2)

# fibonacci(1, 0)

# Finding the nth Fibonacci Number using Recursion | F(n) = F(n-1) + F(n-2):
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(5))
# ------------------------------------------------------------------------------------------------------------------------------------------
# Arrays:
    # Bubble Sort
    # Selection Sort
    # Insertion Sort
    # Merge Sort
    # Linear Search
    # Binary Search

# ------------------------------------------------------------------------------------------------------------------------------------------
# Linked Lists:
    # Linked Lists
    # Linked Lists in Memory
    # Linked Lists Types

# ------------------------------------------------------------------------------------------------------------------------------------------
# Stacks & Queues:
    # Stacks
    # Queues

# ------------------------------------------------------------------------------------------------------------------------------------------
# Hash Tables:
    # Hash Tables
    # Hash Sets
    # Hash Maps

# ------------------------------------------------------------------------------------------------------------------------------------------
# Trees
    # Trees
    # Binary Trees
    # Pre-order Traversal
    # In-order Traversal
    # Post-order Traversal
    # Array Implementation
    # Binary Search Trees
    # AVL Trees

# ------------------------------------------------------------------------------------------------------------------------------------------
# Shortest Path
    # Shortest Path
    # Dijkstra's
    # Bellman-Ford