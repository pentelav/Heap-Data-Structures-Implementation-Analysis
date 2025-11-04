# The algorithm example of Heapsort in Python by constructing a max-heap and executing the steps of extracting the largest element and always upholding the heap property to sort the array in increasing order.

def heapify(arr, n, i):
    largest = i          # Setting the current index as the largest element
    left = 2 * i + 1     # Calculating the left child index
    right = 2 * i + 2    # Calculating the right child index

    # Checking if left child exists and is greater than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Checking if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swapping and continuing heapifying if the largest is not the current root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Building the max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extracting the largest element one by one and maintaining the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swapping the root with the last element
        heapify(arr, i, 0)               # Re-heapifying the reduced heap


# Displaying the original and sorted arrays
data = [12, 11, 13, 5, 6, 7]
print("Original Array:", data)
heap_sort(data)
print("Sorted Array:", data)

