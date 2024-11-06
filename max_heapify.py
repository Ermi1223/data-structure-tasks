def max_heapify(arr, i, n):
    largest = i            # Initialize largest as root
    left = 2 * i + 1       # Left child index
    right = 2 * i + 2      # Right child index

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        max_heapify(arr, largest, n)

# Example usage:
arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]  # Array representation of a binary tree
n = len(arr)
i = 0  # Index of the root of the subtree you want to heapify

max_heapify(arr, i, n)  # Calling the function with defined variables
print(arr)  # Output should show the array with max-heap property maintained for the subtree at index i
