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

def heapify(arr):
    n = len(arr)
    # Start from the last non-leaf node and go upwards
    for i in range((n // 2) - 1, -1, -1):
        max_heapify(arr, i, n)

def heapsort(arr):
    n = len(arr)
    # Step 1: Convert the array into a max-heap
    heapify(arr)
    
    # Step 2: Repeatedly extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Restore the max-heap property for the reduced heap
        max_heapify(arr, 0, i)

# Example usage:
arr = [3, 9, 2, 1, 4, 5]
heapsort(arr)
print("Sorted array:", arr)
