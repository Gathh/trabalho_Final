def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


def insertion_sort(arr, key=lambda x: x):
    arr = arr[:]
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and key(arr[j]) > key(x):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = x

    return arr