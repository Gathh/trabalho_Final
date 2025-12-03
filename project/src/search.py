def linear_search(arr, target, key=lambda x: x):
    for i, item in enumerate(arr):
        if key(item) == target:
            return i
    return -1


def binary_search(arr, target, key=lambda x: x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if key(arr[mid]) == target:
            return mid
        elif key(arr[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1