# HEAP Data Structures: Implementation, Analysis and applications.
## Overview
The project is devoted to implementation and analysis of the algorithms based on heaps, i.e., Heapsort and Priority Queue, that were created during the course Algorithms and Data Structures (MSCS-532-B01). This work aims to show how efficient, designed, and used heap data structures can be used in sorting and task scheduling operations.
## How to Run the Code
There are two Python coding scripts in the repository: one code to perform and test Heapsort, and another one is the Priority Queue code that utilizes Max-Heap structure. The programs may be run in any Python enabled IDE or on the command-line interface.
## Steps to Execute
1. Clone the repository in to a personal computer.
2. Any Python supporting environment can be used to access the project directory.
3. Run the Heapsort program 
4. Execution of the Priority Queue program.
5. Look at the results in the console and see the results of the sorting process and scheduling of tasks.
This does not require any external dependencies except the standard library of Python.
## Summary of Findings
Through the analysis it can be seen that Heapsort is capable of always running with a time complexity of O(n log n) as seen in all input conditions such as sorted, random and reverse-sorted data. The algorithm works in place and has O(1) auxiliary space and is stable under varying data distributions.
Under the implementation of Priority Queue, basic operations of the queue like insertion, extracting the maximum, increasing the key require O(log n) time, whereas the is-empty operation requires O(1) time. The Max-Heap allows the highest-priority element to be stored in the root to allow an effective process of scheduling tasks and resource allocation.
It has been demonstrated through comparative analysis that, on average, Quicksort is the fastest due to cache efficiency, but may actually be of O(n^2) average when not randomised. merge Sort has a constant performance of O(n log (n) yet with additional O(n) memory space. Heapsort is also a good choice because of its good reliability and deterministic time complexity especially in a system where predictability of the execution time is important such as real time scheduling and priority processing.
