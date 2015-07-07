def sel(a):
    for i in range(0, len(a) - 1):
        smallest = i
        for j in range(i, len(a)):
            if (a[smallest] > a[j]):
                smallest = j
        temp = a[smallest]
        a[smallest] = a[i]
        a[i] = temp
    return a


print(sel([4,5,3,2,1,5,0]))
