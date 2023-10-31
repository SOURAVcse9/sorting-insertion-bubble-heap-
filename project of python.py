
#heapsort
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

#bubblesort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#insertionsort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Main function
if __name__ == "__main__":
    numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

    print("1. Heap Sort\n2. Bubble Sort\n3. Insertion Sort")
    choice = int(input("Enter your choice of sorting algorithm: "))

    if choice == 1:
        sorted_numbers = heap_sort(numbers.copy())
        print("Sorted Numbers using Heap Sort:", sorted_numbers)
    elif choice == 2:
        sorted_numbers = bubble_sort(numbers.copy())
        print("Sorted Numbers using Bubble Sort:", sorted_numbers)
    elif choice == 3:
        sorted_numbers = insertion_sort(numbers.copy())
        print("Sorted Numbers using Insertion Sort:", sorted_numbers)
    else:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")
