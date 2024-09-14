// Data Structures & Algorithms in Java Programming Language
// ------------------------------------------------------------------------------------------------------------------------------------------
// Fibonacci Example using (For/While Loop):

// For Loop:
// public class dsa {
//     public static void main(String[] args) {
//         int prev2 = 0;
//         int prev1 = 1;

//         System.out.println(prev2);
//         System.out.println(prev1);

//         for (int fibo = 0; fibo < 18; fibo++) {
//             int newFibo = prev1 + prev2;
//             System.out.println(newFibo);
//             prev2 = prev1;
//             prev1 = newFibo;
//         }

//     } // main method
// } // dsa class


// Recursion (A function that calls itself):
// public class dsa {
//     static int count = 2;

//     public static void fibonacci(int prev1, int prev2) {
//         if (count <= 19) {
//             int newFibo = prev1 + prev2;    // calculate the next Fibonacci number
//             System.out.println(newFibo);    // print the next Fibonacci number
//             prev2 = prev1;
//             prev1 = newFibo;
//             count += 1;
//             fibonacci(prev1, prev2);
//         } else {
//             return;
//         }
//     } // fibonacci method

//     public static void main(String[] args) {
//         System.out.println(0);                  // First Fibonacci Number
//         System.out.println(1);                  // Second Fibonacci Number
//         fibonacci(1, 0);              // Start with 1 and 0
//     } // main method
// } // dsa class


// Finding the nth Fibonacci Number using Recursion | F(n) = F(n-1) + F(n-2):
// public class dsa {
//     public static int F(int n) {
//         if (n <= 1) {
//             return n;
//         } else {
//             return F(n-1) + F(n-2);
//         }
//     } // int method

//     public static void main(String[] args) {
//         System.out.println(F(5));
//     } // main method
// } // dsa class

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