// Data Structures & Algorithms in C Programming Language
// ------------------------------------------------------------------------------------------------------------------------------------------
// Fibonacci Example using (For/While Loop):

// For Loop:
// #include <stdio.h>

// int main() {
//     int prev2 = 0, prev1 = 1;
//     int newFibo;

//     printf("%d\n", prev2);
//     printf("%d\n", prev1);

//     for (int fibo = 0; fibo < 18; fibo++) {
//         newFibo = prev1 + prev2;
//         printf("%d\n", newFibo);
//         prev2 = prev1;
//         prev1 = newFibo;
//     }

//     return 0;
// } // main


// Recursion (A function that calls itself):
// #include <stdio.h>
// int count = 2;

// void fibonacci(int prev1, int prev2) {
//     if (count <= 19) {
//         int newFibo = prev1 + prev2;
//         printf("%d\n", newFibo);
//         prev2 = prev1;
//         prev1 = newFibo;
//         count += 1;
//         fibonacci(prev1, prev2);
//     } else {
//         return;
//     }
// }

//     int main() {
//         printf("0\n");
//         printf("1\n");
//         fibonacci(1, 0);
//         return 0;
//     }


// Finding the nth Fibonacci Number using Recursion | F(n) = F(n-1) + F(n-2):
// #include <stdio.h>

// int F(int n) {
//     if (n <= 1) {
//         return n;
//     } else {
//         return F(n - 1) + F(n - 2);
//     }
// }

// int main() {
//     printf("%d\n", F(5));
//     return 0;
// }


// ------------------------------------------------------------------------------------------------------------------------------------------
// Arrays:
    // Bubble Sort
    // Selection Sort
    // Insertion Sort
    // Merge Sort
    // Linear Search
    // Binary Search

// ------------------------------------------------------------------------------------------------------------------------------------------
// Linked Lists:
    // Linked Lists
    // Linked Lists in Memory
    // Linked Lists Types

// ------------------------------------------------------------------------------------------------------------------------------------------
// Stacks & Queues:
    // Stacks
    // Queues

// ------------------------------------------------------------------------------------------------------------------------------------------
// Hash Tables:
    // Hash Tables
    // Hash Sets
    // Hash Maps

// ------------------------------------------------------------------------------------------------------------------------------------------
// Trees
    // Trees
    // Binary Trees
    // Pre-order Traversal
    // In-order Traversal
    // Post-order Traversal
    // Array Implementation
    // Binary Search Trees
    // AVL Trees

// ------------------------------------------------------------------------------------------------------------------------------------------
// Shortest Path
    // Shortest Path
    // Dijkstra's
    // Bellman-Ford