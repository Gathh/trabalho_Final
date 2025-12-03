def merge_sort(a, key=lambda x: x):
    if len(a) <= 1:
        return a[:]

    mid = len(a) // 2
    L = merge_sort(a[:mid], key)
    R = merge_sort(a[mid:], key)

    i = j = 0
    out = []

    while i < len(L) and j < len(R):
        if key(L[i]) <= key(R[j]):
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1

    return out + L[i:] + R[j:]


def insertion_sort(a, key=lambda x: x):
    arr = a[:]
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(x):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr