# The results of comparing performance of Heapsort, Quicksort (built-in TimSort in Python) and Merge Sort with varying input sizes and measuring and plotting the runtime of each sort can be used to compare the performance of these algorithms.

import random, time
from heapq import heapify, heappop

# Implementing Heapsort algorithm
def heap_sort(arr):
    n = len(arr)
    # Building the max heap from the given array
    for i in range(n // 2 - 1, -1, -1):
        heapify_custom(arr, n, i)
    # Extracting elements from the heap one by one and maintaining the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]     # Swapping the root with the last element
        heapify_custom(arr, i, 0)           # Re-heapifying the reduced heap

# Maintaining the heap property
def heapify_custom(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    # Checking if left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Checking if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    # Swapping and continuing heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_custom(arr, n, largest)

# Comparing sorting algorithms for given input size
def compare_sorts(n):
    # Generating random data of size n
    data = [random.randint(0, 100000) for _ in range(n)]

    # Copying data for fair comparison
    arr1 = data[:]
    arr2 = data[:]
    arr3 = data[:]

    # Measuring Heapsort execution time
    start = time.time()
    heap_sort(arr1)
    heap_time = time.time() - start

    # Measuring Quicksort (Python’s built-in TimSort) execution time
    start = time.time()
    arr2.sort()
    quick_time = time.time() - start

    # Measuring Merge Sort execution time
    start = time.time()
    merge_sort(arr3)
    merge_time = time.time() - start

    # Displaying results
    print(f"n={n}: Heapsort={heap_time:.5f}s, Quicksort={quick_time:.5f}s, Mergesort={merge_time:.5f}s")

# Implementing Merge Sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        # Recursively sorting left and right halves
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # Merging sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Adding remaining elements
        arr[k:] = L[i:] + R[j:]

# Running the comparison for different input sizes
for size in [1000, 5000, 10000, 50000]:
    compare_sorts(size)
