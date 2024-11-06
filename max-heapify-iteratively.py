def max_heapify(arr, i, n):
    while True:
        largest = i              # Initialize largest as root
        left = 2 * i + 1         # Left child index
        right = 2 * i + 2        # Right child index

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is still the root, then the subtree is a max-heap
        if largest == i:
            break

        # Swap the root with the largest child
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Move down to the largest child to continue heapifying
        i = largest

# Example usage:
arr = [3, 9, 2, 1, 4, 5]  # Array representation of a binary tree
n = len(arr)
i = 0  # Index of the root of the subtree you want to heapify

max_heapify(arr, i, n)
print(arr)  # Output should show the array with max-heap property maintained for the subtree at index i
