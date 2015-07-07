def so(arr):
    for i in range(2, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(so([31, 41, 59, 26, 41, 58]))
